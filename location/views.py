from django.shortcuts import render, redirect
import requests
import json

# Create your views here.
def index(request):

    ip = requests.get('https://api.ipify.org?format=json')
    ip_data= json.loads(ip.text)
    response = requests.get('http://ip-api.com/json/'+ ip_data["ip"])
    response_data= response.text
    location_data= json.loads(response_data)
    return render(request, 'base.html', {'data': location_data})