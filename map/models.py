from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns

class Planner(models.Model):  
    # Model representing name location  
    location = models.CharField(max_length = 30)
    stay_time = models.FloatField(default=0)
    #start time that user want to go in each place
    times = models.CharField(max_length = 30,default="")
    date = models.CharField(max_length = 20,default="")
    
    def __str__(self):
        return f'{self.location}, {self.stay_time}, {self.date},{self.time}'
    def get_absolute_url(self):
        return reverse('planner-detail', args=[str(self.id)])

class Users(models.Model):

    email = models.CharField(max_length = 30)

    # User can have multi-plan
    plans = models.ForeignKey('Planner', on_delete=models.SET_NULL, null=True)
    
    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.id)])

    def __str__(self):

        return f'{self.email}, {self.plans}'

