from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import Response, JSONResponse

app = FastAPI()

class typeCars(BaseModel):
    id: str
    brand: str
    model: str

garage: List[typeCars] = []


def voiture():
    cars_converted = []
    for cars in garage:
        cars_converted.append(cars.model_dump())
    return cars_converted

@app.get("/ping")
def hello():
    return Response(content="pong", status_code=200, media_type="text/plain")

@app.get("/ping")
def root():
    return Response(content="pong", status_code=200, media_type="text/plain")

@app.post("/cars")
def create_car(cars_payload: List[typeCars]):
    garage.extend(cars_payload)
    return JSONResponse(content=voiture(), status_code=201)

@app.get("/cars")
def list_cars():
    return {"cars": voiture()}

