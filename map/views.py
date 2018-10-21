from django.shortcuts import render
from .models import Location
import urllib.request
import json
import ssl

api_key = 'AIzaSyBENVTYtp6UnlTVs8gmLomS1NNlJqK7-ww'

def index(request):
    if request.method == 'POST':
          if request.POST.get('location') and request.POST.get('stay_time'):
                post= Location()
                post.location= request.POST.get('location')
                post.stay_time= request.POST.get('stay_time')
                post.save()
                
                return render(request, 'index.html')  
    else:
        return render(request,'index.html')

def search_place(search):
    endpoint = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?'
    inputtype = 'textquery&fields=formatted_address,name,opening_hours&locationbias=circle:2000@47.6918452,-122.2226413'
    context = ssl._create_unverified_context()
    
    text_request = endpoint + f'input={search}&inputtype={inputtype}&key={api_key}'

    response = urllib.request.urlopen(text_request, context=context).read()
    direction = json.loads(response.decode('utf-8'))
    
    place  = direction['candidates'][0]['formatted_address']
    return HttpRequest(place)

def  time_count(origin, destination, mode):
    endpoint = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
    context = ssl._create_unverified_context()

    text_request = endpoint + f'origins={origin}&destinations={destination}&mode={mode}&key={api_key}'

    response = urllib.request.urlopen(request, context=context).read()
    direction = json.loads(response.decode('utf-8'))

    time = direction['rows'][0]['elements'][0]['duration']['text'])
    return HttpRequest(time)



 
    