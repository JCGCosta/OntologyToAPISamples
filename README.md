# OntologyToAPISamples

> This repository contains some samples of implementations using the ontologytoapi python package.

## Current Use Cases:

- **WeatherMonitoring**: A simple weather information retrieval API.

<img src="https://github.com/JCGCosta/OntologyToAPISamples/blob/main/UseCases/WeatherMonitoring_UseCase/RealizationOntologies/WeatherMonitoringOntologyDiagram.jpg?raw=true" alt="WeatherMonitoring" title="Abstract Ontology Classes.">

- **PB_UseCase**: A Local Electricity Market use case.

<img src="https://github.com/JCGCosta/OntologyToAPISamples/blob/main/UseCases/PB_UseCase/RealizationOntologies/PB_UseCaseOntologyDiagram.jpg?raw=true" alt="PB_UseCase" title="Abstract Ontology Classes.">

## Installation and Running:

### Step 1: Pre-requisites

- Make sure you have Python installed on your system. You can download Python from the official website: [Python Downloads](https://www.python.org/downloads/).
- Ensure you have a MongoDB instance running. You can download MongoDB from the official website: [MongoDB Downloads](https://www.mongodb.com/try/download/community). We recommend using MongoDB Compass for easier management.
- Ensure you have a MySQL instance running. You can download MySQL from the official website: [MySQL Downloads](https://dev.mysql.com/downloads/mysql/).

### Step 2: Creating a Virtual Environment (If wanted, else skip to Step 3)

```bash
# Create a virtual environment named 'venv'
python -m venv venv

# Activate the virtual environment (If you are on Windows)
.\venv\Scripts\activate

# Activate the virtual environment (If you are on Linux)
source venv/bin/activate
```

### Step 3: Installing Dependencies

```bash
# Now inside the environment install the libraries from the requirements.txt
pip install -r requirements
```

### Step 3: Before Running

- Before running the samples, make sure to configure the database connection details in the respective realization ontology files.

```turtle
###  In the SmartLEM-PB_LEM.ttl realization ontology:
pbuc:DatabaseCommunication_R rdf:type owl:NamedIndividual ,
                                      <http://www.cedri.com/SmartLEM-Communications#DatabaseCommunication> ;
                             <http://www.cedri.com/SmartLEM-Communications#hasConnectionString> "mysql+aiomysql://<username>:<password>@<ipaddress>:<port>/<database_name>" ;
                             <http://www.cedri.com/SmartLEM-Communications#usesTechnology> "MYSQL" .
```

```turtle
###  In the SmartLEM-WeatherBusinessModel.ttl realization ontology:
wmuc:DatabaseCommunication_R rdf:type owl:NamedIndividual ,
                                      <http://www.cedri.com/SmartLEM-Communications#DatabaseCommunication> ;
                             <http://www.cedri.com/SmartLEM-Communications#hasConnectionString> "mongodb://<ipaddress>:<port>/<collection_name>" ;
                             <http://www.cedri.com/SmartLEM-Communications#usesTechnology> "MONGODB" .
```

- Its also necessary to configure and to populate the databases to see some results, for that we provide some scripts inside each use case folder.

```bash
# First, rename the .env_example file to .env and set the database connection details.
cp .env_example .env
echo "MYSQL_IP_ADDRESS=<your_mysql_ip_address>
MYSQL_PORT=<your_mysql_port>
MYSQL_USERNAME=<your_mysql_username>
MYSQL_PASSWORD=<your_mysql_password>
" > .env

# Run the respective database setup script for the PB_UseCase.
python UseCases/PB_UseCase/setupSQL/create_pb_use_case.py

# Run the respective database setup script for the PB_UseCase.
python UseCases/WeatherMonitoring_UseCase/setupSQL/create_weather_use_case.py
```

### Step 4: Running Samples

- At this point you are ready to run the samples, just be aware that both use cases are being loaded in the runAPI.py file, so if you want to run only one use case you will need to comment the other(s):

```bash
python runAPI.py
```

### Step 5: Results

- Once the API is running, you can access the endpoints using a web browser or tools like Postman or curl.

- The browser swagger documentation will look like this:

<img src="https://github.com/JCGCosta/OntologyToAPISamples/blob/main/UseCases/APIDocs.png?raw=true" alt="APIDocs" title="Abstract Ontology Classes.">
