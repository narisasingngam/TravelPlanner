from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns

class Location(models.Model):  
    # Model representing name location  
    location = models.CharField(max_length = 30)
    stay_time = models.IntegerField(default=0)
    # User can have multi-plan
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    #start time that user want to go in each place
    time = models.IntegerField(default=0)
    
    def __str__(self):
        return f'{self.location}, {self.stay_time}, {self.user},{self.time}'
    def get_absolute_url(self):
        return reverse('planner-detail', args=[str(self.id)])

class User(models.Model):

    email = models.CharField(max_length = 30)
    date = models.DateField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.email}, {self.date}'
