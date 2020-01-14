from django.shortcuts import render
import json
import requests

def home(request):

    if request.method == "POST":
        city_name = request.POST['city_name']
        api_request = requests.get("http://api.airvisual.com/v2/nearest_city?key=8b5e9c27-7e2c-4526-9b56-fb94072dd54d")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."   

        return render(request, 'home.html', {'api': api})



    else:
        api_request = requests.get("http://api.airvisual.com/v2/nearest_city?key=8b5e9c27-7e2c-4526-9b56-fb94072dd54d")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."   

        return render(request, 'home.html', {'api': api})

def about(request):
    return render(request, 'about.html', {})