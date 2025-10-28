from sqlalchemy import create_engine, text
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("MYSQL_USERNAME")
password = os.getenv("MYSQL_PASSWORD")
host = os.getenv("MYSQL_IP_ADDRESS")
port = os.getenv("MYSQL_PORT")

engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/")

print(f"Connected to {host}:{port} with the following credentials: {username}:{password}.")

# Read and execute the SQL file
with open("pb_LEM_SQL_database.sql", "r") as file:
    sql_script = file.read()

commands = [cmd.strip() for cmd in sql_script.split(";") if cmd.strip()]

conn = engine.connect()
transaction = conn.begin()
for command in commands:
    conn.execute(text(command))
transaction.commit()
conn.close()

print("Database and schema created and populated successfully.")

df = pd.read_csv("Datasets/AggregatedUseCase.csv", sep="\t")

db_engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}:{port}/PB_LEM?charset=utf8mb4"
)

df.columns = df.columns.str.upper()
df=df.rename(columns = {'MEMBER':'MEMBER_ID', "UTC_TIMESTAMP":"UTC_T"})

if "UTC_T" in df.columns:
    df["UTC_T"] = pd.to_datetime(df["UTC_T"], utc=True, dayfirst=True, errors="coerce").dt.tz_convert(None)

numeric_cols = [
    "MEMBER_ID",
    "ELECTRICITY_LOAD",
    "RESIDENTIAL_ELECTRICITY_PRICE",
    "RESIDENTIAL_SOLAR_GENERATION",
    "RESIDENTIAL_WIND_GENERATION",
    "TEMPERATURE",
    "RELATIVE_HUMIDITY",
]
for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

print(df.head())

with db_engine.begin() as conn:
    df.to_sql(
        "lem_data",
        con=conn,
        if_exists="append",
        index=False,
        chunksize=1000,
        method="multi",
    )

print(f"Inserted {len(df)} rows into PB_LEM.LEM_DATA successfully.")
