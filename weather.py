from dotenv import load_dotenv
from flask import request, render_template, Flask
from dataclasses import dataclass
import requests
import os

load_dotenv()
api_key = os.getenv('Api_key')


@dataclass
class WeatherData:
    def __init__(self, api_main, description, icon, temperature, humidity):
        self.api_main = api_main
        self.description = description
        self.icon = icon
        self.temperature = temperature
        self.humidity = humidity

    def __str__(self):
        return (f"Weather: {self.api_main}, Description: {self.description}, "
                f"Icon: {self.icon}, Temperature: {self.temperature}°C, "
                f"Humidity: {self.humidity}%")
    


def get_lanlon(city_name, state_code, country_code, Api_key):
    response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}, {state_code}, {country_code}&appid={Api_key}').json()
    data = response[0]
    lat, lon = data.get('lat'), data.get('lon')
    return lat, lon

# get weather conditions
def get_current_weather(lat, lon, Api_key):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={Api_key}&units=metric').json()
    # print(response)
        
    data = WeatherData(
    api_main = response.get('weather')[0].get('main'),
    description = response.get('weather')[0].get('description'),  # Correct spelling here
    icon = response.get('weather')[0].get('icon'),
    temperature = int(response.get('main').get('temp')),
    humidity = response.get('main').get('humidity')
    )

    return data



def main(city_name, state_name, country_name, api_key):
    lat, lon = get_lanlon(city_name, state_name, country_name, api_key)
    weather_data = get_current_weather(lat, lon, api_key)
    return weather_data
                         

if __name__ == "__main__":
    lat, lon = get_lanlon('Toronto', 'ON', 'Canada', api_key)
    print(get_current_weather(lat, lon, api_key))
    