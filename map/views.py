from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views import generic
import urllib.request
import json
import ssl
from map import ptime

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
        
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def search_place(request):
    if request.method == 'POST':
        json_body = json.loads(request.body.decode('utf-8'))
        place = json_body['place']

        endpoint = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?'
        inputtype = 'textquery&fields=formatted_address,name,opening_hours&locationbias=circle:2000@47.6918452,-122.2226413'
        request = endpoint + f'input={place}&inputtype={inputtype}&key={api_key}' 

        context = ssl._create_unverified_context()
        response = urllib.request.urlopen(request, context=context).read()
        direction = json.loads(response.decode('utf-8'))

        return HttpResponse(direction['candidates'][0]['formatted_address'])

@csrf_exempt
def  time_count(request):
    if request.method == 'POST':
        json_body = json.loads(request.body.decode('utf-8'))
        origin = json_body['origin']
        destination = json_body['destination']
      
        endpoint = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
        request = endpoint + f'origins={origin}&destinations={destination}&mode=driving&key={api_key}'
        
        context = ssl._create_unverified_context()
        response = urllib.request.urlopen(request, context=context).read()
        direction = json.loads(response.decode('utf-8'))
        time_str = direction['rows'][0]['elements'][0]['duration']['text']
        
        time_int = ptime.int_time(time_str)

        return JsonResponse(json.dumps(time_int), safe = False)

@csrf_exempt
def  auto_complete(request):
    if request.method == 'POST':
        json_body = json.loads(request.body.decode('utf-8'))
        text = json_body['text']
      
        endpoint = 'https://maps.googleapis.com/maps/api/place/autocomplete/json?'
        request = endpoint + f'input={text}&types=establishment&language=en&key={api_key}'
        
        context = ssl._create_unverified_context()
        response = urllib.request.urlopen(request, context=context).read()
        predict = json.loads(response.decode('utf-8'))

        return JsonResponse(predict)

@csrf_exempt
def remaining_time(request):
    if request.method == 'POST':

        json_body = json.loads(request.body.decode('utf-8'))
        spend_time = json_body['duration']
        time_remain = json_body['remaining']

        time = int(time_remain)-int(spend_time)
        return JsonResponse(json.dumps(time),safe=False)

array_place = []

@csrf_exempt
def  time_place(request):
    if request.method == 'POST':
        json_body = json.loads(request.body.decode('utf-8'))
        place = json_body['place']
        k = ""

        array_place.append(place)

        if(len(array_place) == 2):
             k = array_place.pop(0)

             endpoint = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
             request = endpoint + f'origins={k}&destinations={place}&mode=driving&key={api_key}'
        
             context = ssl._create_unverified_context()
             response = urllib.request.urlopen(request, context=context).read()
             direction = json.loads(response.decode('utf-8'))
             time_str = direction['rows'][0]['elements'][0]['duration']['text']
        
             time_int = ptime.int_time(time_str)
        else:
             time_int = 0   
        return JsonResponse(json.dumps(time_int), safe = False)  

