from django.urls import path
from map import views


urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search_place, name='place'),
    path('time/', views.time_count, name='time')
]