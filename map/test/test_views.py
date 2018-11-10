from django.test import TestCase
from django.urls import reverse
from django.http import JsonResponse
import urllib.request
# import requests
from map import ptime,views
import json
import ssl

# class TestMethodsInViews(TestCase):

#     def test_connect_server(self):
#         '''
#         test connect server
#         '''
#         response = self.client.get('')
#         self.assertEquals(response.status_code, 200)

#     def test_get_response(self):
#         # data = json.dumps({"duration" : "1", "remaining" : "2.4", "road" : "2 hours"})

#         response = self.client.post(reverse('travelplanner:remain'))
#         self.assertEquals(response.status_code, 200)

#         # datap = json.dumps({"place" : "pattaya"})
#         response1 = self.client.post(reverse('travelplanner:place'))
#         self.assertEquals(responde.status_code, 200)

    # def test_time_remain(self):
    #     data = json.dumps({"duration" : "1", "remaining" : "2.4", "road" : "2 hours"})
    #     response = self.client.post(reverse('travelplanner:remain'), {"form":data}, 'application/json')
    #     self.assetNotContains(response,'error')


        



