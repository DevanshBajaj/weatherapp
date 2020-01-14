from django.shortcuts import render
import json
import requests

def home(request):

    if request.method == "POST":
        city_name = request.POST['city_name']
        api_request = requests.get("http://api.openweathermap.org/data/2.5/weather?q=" + city_name + "&units=metric&APPID=d0a3abf9e9950b930853deff99063689")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."   

        return render(request, 'home.html', {'api': api})



    else:
        api_request = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Ghaziabad&units=metric&appid=d0a3abf9e9950b930853deff99063689")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."   

        return render(request, 'home.html', {'api': api})

def about(request):
    return render(request, 'about.html', {})