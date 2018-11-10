from django.urls import path
from map import views
from map.views import *

app_name = 'travelplanner'

urlpatterns = [
    path('', views.index, name='index'),
<<<<<<< HEAD
    path('time-remain/',views.remaining_time, name='remain'),
=======
    # path('time/', views.remaining_time, name='time'),
    # path('auto-complete/',views.auto_complete, name='auto'),
    path('time-remain/',views.remaining_time, name='duration'),
>>>>>>> 8f599f374e0d9516100d399fb5999cc21b16973b
    path('place/',views.time_place, name='place')
]