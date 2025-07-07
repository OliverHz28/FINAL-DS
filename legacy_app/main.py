from fastapi import FastAPI
from new_microservice.service import service_response

app = FastAPI()

@app.get("/data")
def get_data():
        response = service_response()
        return {
            "message": "Datos obtenidos desde el servicio.",
            "service_response": response
        }
