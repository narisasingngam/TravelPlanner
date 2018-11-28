import logging
# for file logging
logging.basicConfig(filename='file.log'
                    ,level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M'
                    )

from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views import generic
from django.core import serializers
import urllib.request
import json
import ssl
from decouple import config
from map import ptime
from map.models import Planner,Users


API_KEY = config('API_KEY')


# set up for logging
console = logging.StreamHandler()
console.setLevel(logging.INFO)

formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')

console.setFormatter(formatter)

logging.getLogger('').addHandler(console)

logger = logging.getLogger('logger')


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
def remaining_time(request):   
    if request.method == 'POST':
        try:    
            json_body = json.loads(request.body.decode('utf-8'))
            spend_time = float(json_body['spendtime'])
            time_remain = float(json_body['remaining'])
            road_time = ptime.int_time(json_body['road'])

            time = (int(time_remain) - int(road_time) - int(spend_time)) + ((time_remain - int(time_remain))*100/60 - (road_time - int(road_time))*100/60 - (spend_time - int(spend_time))*100/60)
            print(time)
       
            remain = int(time) + (time - int(time))*60/100 

            logger.info(f'remaining time : {remain}')

        except:
                logger.error(sys.exc_info())
        
        return JsonResponse(json.dumps(float(f"{remain:.2f}")),safe=False)

        
@csrf_exempt
def time_place(request):
    if request.method == 'POST':
        try:        

            json_body = json.loads(request.body.decode('utf-8'))
            place = json_body['place']
            place_without_space = place.replace(" ","%20")
        
            origin_place = json_body['origin']
            origin_place_non_space = origin_place.replace(" ","%20")

            endpoint = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
            request = endpoint + f'origins={origin_place_non_space}&destinations={place_without_space}&mode=driving&key={API_KEY}'
        
            context = ssl._create_unverified_context()
            response = urllib.request.urlopen(request, context=context).read()
            direction = json.loads(response.decode('utf-8'))
            time_str = direction['rows'][0]['elements'][0]['duration']['text']

            logger.info(f"duration between {place} and {origin_place} : {time_str}")
     
        except:
                logger.error(sys.exc_info())
   
        return JsonResponse(time_str, safe=False) 

@csrf_exempt  
def search_place(request):  
     if request.method == 'POST': 
        try:
               json_body = json.loads(request.body.decode('utf-8'))  
               place = json_body['place']
               place_without_space = place.replace(" ","%20")  
  
               endpoint = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?'  
               inputtype = 'textquery&fields=formatted_address,name,opening_hours&locationbias=circle:2000@47.6918452,-122.2226413'  
               request = endpoint + f'input={place_without_space}&inputtype={inputtype}&key={API_KEY}'   
  
               context = ssl._create_unverified_context()  
               response = urllib.request.urlopen(request, context=context).read()  
               direction = json.loads(response.decode('utf-8'))
               address =   direction['candidates']

               logger.info(f'search: {address}')

        except:

                logger.error(sys.exc_info())

  
        return JsonResponse(address, safe=False)

@csrf_exempt
def savedata(request):
        if request.method == 'POST':
           try:
                json_body = json.loads(request.body.decode('utf-8'))
                email = json_body['email']
                location = json_body['location']
                spendtime = json_body['spendtime']
                times = json_body['times']
                date = json_body['date']
                duration = json_body['duration']
                name_planner = json_body['name']
                id_plan = json_body['id']
                data_plan = Planner(location=location,date=date,times=times,duration=duration,spend_time=spendtime,name_planner=name_planner,id_plan=id_plan)
                data_plan.save()
                user = Users(email=email,plans=data_plan)
                user.save()

                logger.info(f'{data_plan} saved!')
           except:
                logger.error(sys.exc_info())

           return JsonResponse(email,safe=False)

@csrf_exempt
def user_data(request):
        if request.method == 'POST':
            try:    
                json_body = json.loads(request.body.decode('utf-8'))
                email = json_body['email']
                user = Users.objects.filter(email=email)
                list = []
                #show user
                for i in user:
                        to_json = {
                                "date" : i.plans.date,
                                "name" : i.plans.name_planner,
                                "id" : i.plans.id_plan
                        }
                        if(to_json not in list):
                                # print(to_json)
                                list.append(to_json)
                                # print(list)
                                # print(i.plans.date)
                                logger.info(f'add {to_json}')                

            except:
                    logger.error(sys.exc_info())                    
            return JsonResponse(list,safe=False)

@csrf_exempt
def plan_data(request):
        list = []
        if request.method == 'POST':
            try:    
                json_body = json.loads(request.body.decode('utf-8'))
                email = json_body['email']
                id_plan = json_body['id']
                user = Users.objects.filter(email=email)
                # show plan     
                for i in user:

                        if(i.plans.id_plan == id_plan):
                                to_json = {
                                "id" : i.plans.id_plan,
                                "email" : i.email,
                                "date" : i.plans.date,
                                "name" : i.plans.name_planner,
                                "location" : i.plans.location,
                                "spendtime" : i.plans.spend_time,
                                "times" : i.plans.times,
                                "duration" : i.plans.duration,
                                "remaining" : i.plans.total_time
                                }
                                list.append(to_json)
                                print(to_json)
                                logger.info(to_json)
            except: 
                logger.error(sys.exc_info())                        

            return JsonResponse(list,safe=False)
