from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns

class Planner(models.Model):  
    # Model representing name location  
    location = models.CharField(max_length = 60)
    spend_time = models.CharField(max_length = 30,default="0")
    #start time that user want to go in each place
    duration = models.CharField(max_length = 30,default="0")
    times = models.CharField(max_length = 30,default="")
    date = models.CharField(max_length = 20,default="")
    name_planner = models.CharField(max_length =30,default="")
    id_plan = models.CharField(max_length=20,default="")
    
    def __str__(self):
        return f'{self.location}, {self.spend_time},{self.duration}, {self.date},{self.times}'
    def get_absolute_url(self):
        return reverse('planner-detail', args=[str(self.id)])

class Users(models.Model):

    email = models.CharField(max_length = 30)

    # User can have multi-plan
    plans = models.ForeignKey('Planner', on_delete=models.SET_NULL, null=True)
    
    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.id)])

    def __str__(self):

        return f'{self.email},{self.plans}'

