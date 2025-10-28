import uvicorn
from OntologyToAPI.core.APIGenerator import APIGenerator

if __name__ == "__main__":
    APIGen = APIGenerator(showLogs=True)
    APIGen.load_ontologies(paths=[
        "UseCases/PB_UseCase/RealizationOntologies/SmartLEM-PB_LEM.ttl",
        "UseCases/PB_UseCase/RealizationOntologies/SmartLEM-EqualProsumerBiddingBusinessModel.ttl"
    ])
    APIGen.load_ontologies(paths=[
        "UseCases/WeatherMonitoring_UseCase/RealizationOntologies/SmartLEM-Weather_LEM.ttl",
        "UseCases/WeatherMonitoring_UseCase/RealizationOntologies/SmartLEM-WeatherBusinessModel.ttl"
    ])
    APIGen.serialize_ontologies()
    api_app = APIGen.generate_api_routes()
    uvicorn.run(api_app, host="127.0.0.1", port=5000)