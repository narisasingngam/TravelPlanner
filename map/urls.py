from django.urls import path
from map import views


urlpatterns = [
    path('', views.index, name='index'),
    # path('test/',views.test_database)
]