from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from weather import api_get_wearher, api_geo_city
class WeatherSchema(BaseModel):
    city: str

app = FastAPI()


templates = Jinja2Templates(directory="templates")
@app.get('/')
def get_template(request: Request):
    return templates.TemplateResponse(request=request, name='index.html')


@app.post('/api/weather/post')
def get_temperature(request: Request, data: WeatherSchema):
    data = api_geo_city(data.city)
    geo_lat:str = data[0]['geo_lat']
    geo_lon:str = data[0]["geo_lon"]
    data = api_get_wearher(lat=geo_lat, lon=geo_lon)
    return data["data"]["weatherByPoint"]["now"]



if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app='main:app', host='127.0.0.1', port=8000, reload=True)
