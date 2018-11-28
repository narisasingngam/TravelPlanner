from django.urls import path
from map import views
from map.views import *

app_name = 'travelplanner'

urlpatterns = [
    path('', views.index, name='index'),
    path('time-remain/',views.remaining_time, name='remain'),
    path('place/',views.time_place, name='place'),
    path('savedata/',views.savedata,name='savedata'),
    path('user_data/',views.user_data,name='user'),
    path('plan_data/',views.plan_data,name='plan'),
    path('search/',views.search_place,name='search')
]