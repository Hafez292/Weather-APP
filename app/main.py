from fastapi import FastAPI
import requests

app = FastAPI()

API_KEY = "26afcd28d58e4c1fad182734250507"

@app.get("/weather/{city}")
def get_weather(city: str):
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return {
            "city": data["location"]["name"],
            "temperature": data["current"]["temp_c"],
            "description": data["current"]["condition"]["text"]
        }
    else:
        return {"error": "City not found or API error"}
