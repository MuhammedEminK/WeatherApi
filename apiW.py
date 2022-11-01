

from fastapi import FastAPI
from pydantic import BaseModel
from WeatherApi.weather import Weather
from fastapi.responses import PlainTextResponse

class Coordinate(BaseModel):
    lat:str
    lon:str


app = FastAPI()


@app.post("/hourse")
async def hourse(item: Coordinate):
    w = Weather(key="efa355ad3c0153106e4889cd4a833197")
    x = w.hourse(lat=item.lat, lon=item.lon)
    return x

@app.post("/now")
async def now(item: Coordinate,):
    w = Weather(key="efa355ad3c0153106e4889cd4a833197")
    x = w.now(lat=float(item.lat), lon=float(item.lon))

    return x