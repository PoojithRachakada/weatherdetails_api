# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 17:48:22 2021

@author: Poojith
"""
from flask import Flask
import requests

app = Flask(__name__)

#zip codes =07303,67301

api_key="81a74435648b60dd638a40a1613b22d2"

@app.route('/')
def index():
    return "<h1>Welcome to Weather details Api<h1>\
            <p>For details how to use api visit 'localhost:5000/weather'</p>\
            <p>If you know using api here enter your values use the endpoind 'localhost:5000/weather/{Enter value}'</p>"
                
@app.route('/weather')
def weather():
    return "<h1>Details to access weather different parameters</h1>\
            <p>Get details using city_name use '/city name'</p>\
            <p>Get details using city name and state code use '/city name,state code'</p>\
            <p>Get details using city name,state code and country code use '/city name,state code,country code'</p>\
            <p>Get details using zip code use '/zip code'</p>\
            <p>Get details using geographic cordinates use '/latitude,longitude' </p>"

#api call from city name and zip code
@app.route('/weather/<string:city_name>')
def weather_api_split(city_name):
    if(True in [char.isdigit() for char in city_name]):
         return weather_zip(city_name)
    else:
        return weather_name(city_name)
        
def weather_name(city_name):
    api_url="https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city_name,api_key)
    r = requests.get(api_url)
    return r.json()

#api call from city name,state code
@app.route('/weather/<string:city_name>,<string:state_code>')
def weather_name_statecode(city_name,state_code):
    api_url="https://api.openweathermap.org/data/2.5/weather?q={},{}&appid={}".format(city_name,state_code,api_key)
    r = requests.get(api_url)
    return r.json()

#api call from city name,state code,country code
@app.route('/weather/<string:city_name>,<string:state_code>,<string:country_code>')
def weather_name_countrycode(city_name,state_code,country_code):
    api_url="https://api.openweathermap.org/data/2.5/weather?q={},{},{}&appid={}".format(city_name,state_code,country_code,api_key)
    r = requests.get(api_url)
    return r.json()


#api call from zip_code
#@app.route('/weather/<string:zip_code_post>')
def weather_zip(zip_code_post):
    api_url = "https://api.openweathermap.org/data/2.5/weather?zip={}&units=imperial&appid={}".format(zip_code_post, api_key)
    r = requests.get(api_url)
    return r.json()

#api call from geographic coordinates
@app.route('/weather/<int:lat>,<int:lon>')
def weather_cor(lat,lon):
    api_url="https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}".format(lat,lon,api_key)
    r=requests.get(api_url)
    return r.json()

def get_data(zip_code):
    global json_data
    
    

if __name__ == '__main__':
   app.run()


