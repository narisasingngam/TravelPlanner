from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views import generic
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
        
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def search_place(request):
    if request.method == 'POST':
        json_body = json.loads(request.body.decode('utf-8'))
        place = json_body['place']

        endpoint = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?'
        inputtype = 'textquery&fields=formatted_address,name,opening_hours&locationbias=circle:2000@47.6918452,-122.2226413'
        request = endpoint + f'input={place}&inputtype={inputtype}&key={api_key}' 

        response = urllib.request.urlopen
        context = ssl._create_unverified_context()
        response = urllib.request.urlopen(request, context=context).read()
        direction = response.decode('utf-8')

        return JsonResponse(json.loads(direction))

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
        direction = response.decode('utf-8')

        return JsonResponse(json.loads(direction))

@csrf_exempt
def  auto_complete(request):
    if request.method == 'POST':
        json_body = json.loads(request.body.decode('utf-8'))
        text = json_body['text']
      
        endpoint = 'https://maps.googleapis.com/maps/api/place/autocomplete/json?'
        request = endpoint + f'input={text}&types=establishment&language=en&key={api_key}'
        
        context = ssl._create_unverified_context()
        response = urllib.request.urlopen(request, context=context).read()
        predict = response.decode('utf-8')

        return JsonResponse(json.loads(predict))

    