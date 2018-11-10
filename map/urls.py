from django.urls import path
from map import views
from map.views import *

app_name = 'travelplanner'

urlpatterns = [
    path('', views.index, name='index'),
    path('time-remain/',views.remaining_time, name='remain'),
    path('place/',views.time_place, name='place')
]