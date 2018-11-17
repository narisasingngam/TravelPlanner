from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views import generic
from django.core import serializers
import urllib.request
import json
import ssl
from map import ptime
from map.models import Planner,Users

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

        return HttpResponse(direction['candidates'])

@csrf_exempt
def remaining_time(request):
    if request.method == 'POST':
        json_body = json.loads(request.body.decode('utf-8'))
        spend_time = float(json_body['spendtime'])
        time_remain = float(json_body['remaining'])
        road_time = ptime.int_time(json_body['road'])

        time = (int(time_remain) - int(road_time) - int(spend_time)) + ((time_remain - int(time_remain))*100/60 - (road_time - int(road_time))*100/60 - (spend_time - int(spend_time))*100/60)
        print(time)
       
        remain = int(time) + (time - int(time))*60/100 

        return JsonResponse(json.dumps(float(f"{remain:.2f}")),safe=False)

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
def time_place(request):
    if request.method == 'POST':
        json_body = json.loads(request.body.decode('utf-8'))
        place = json_body['place']
        place_without_space = place.replace(" ","%20")
        
        origin_place = json_body['origin']
        origin_place_non_space = origin_place.replace(" ","%20")


        endpoint = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
        request = endpoint + f'origins={origin_place_non_space}&destinations={place_without_space}&mode=driving&key={api_key}'
        
        context = ssl._create_unverified_context()
        response = urllib.request.urlopen(request, context=context).read()
        direction = json.loads(response.decode('utf-8'))
        time_str = direction['rows'][0]['elements'][0]['duration']['text']
     
   
        return JsonResponse(time_str, safe=False) 

@csrf_exempt
def savedata(request):
    if request.method == 'POST':
        json_body = json.loads(request.body.decode('utf-8'))
        email = json_body['email']
        location = json_body['location']
        spendtime = json_body['spendtime']
        times = json_body['times']
        date = json_body['date']
        duration = json_body['duration']
        data_plan = Planner(location=location,date=date,times=times,duration=duration,spend_time=spendtime)
        data_plan.save()
        user = Users(email=email,plans=data_plan)
        user.save()
        return JsonResponse(email,safe=False)

@csrf_exempt
def user_data(request):
        if request.method == 'POST':
                json_body = json.loads(request.body.decode('utf-8'))
                email = json_body['email']
                user = Users.objects.filter(email=email)
                list = []
                #show user
                for i in user:
                        if(i.plans.date not in list):
                                list.append(i.plans.date)
                                print(i.plans.date)
                        else:
                                break
                return JsonResponse(list,safe=False)

@csrf_exempt
def plan_data(request):
        list = []
        if request.method == 'POST':
                json_body = json.loads(request.body.decode('utf-8'))
                email = json_body['email']
                date = json_body['date']
                user = Users.objects.filter(email=email)
                # list = []
                # show plan     
                for i in user:

                        if(i.plans.date == date):
                                show_plan = Planner.objects.filter(date=i.plans.date,location=i.plans.location,times=i.plans.times,duration=i.plans.duration,spend_time=i.plans.spend_time)
                                json_plan = serializers.serialize('json',show_plan)
                                list.append(json_plan)
                                print(json_plan)
                                
                                        # print(j.times+" "+j.location+" "+j.spend_time+" "+j.duration)
        return HttpResponse(list,content_type="application/json")
