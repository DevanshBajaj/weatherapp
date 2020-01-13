from django.shortcuts import render
import json
import requests

def home(request):

    
    api_request = requests.get("http://api.openweathermap.org/data/2.5/weather?id=1273293&units=metric&APPID=d0a3abf9e9950b930853deff99063689")
    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error..."   

    return render(request, 'home.html', {'api': api})

def about(request):
    return render(request, 'about.html', {})