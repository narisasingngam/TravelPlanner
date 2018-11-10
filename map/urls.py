from django.urls import path
from map import views
from map.views import *


urlpatterns = [
    path('', views.index, name='index'),
    # path('time/', views.remaining_time, name='time'),
    # path('auto-complete/',views.auto_complete, name='auto'),
    path('time-remain/',views.remaining_time, name='duration'),
    path('place/',views.time_place, name='place')
]