from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()

@app.post("/service-response")
def service_response():
        return {
            "id": 123,
            "stado": "activo",
            "mensaje": "respuesta exitosa"
        }

@app.get("/service-response")
def service_response():
        return {
            "id": 123,
            "stado": "activo",
            "mensaje": "respuesta exitosa"
        }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5001)