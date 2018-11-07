from django.test import TestCase
from map import *
import json

class TestMethodsInViews(TestCase):
    
    def remain_time(json):
        return f"json.loads(views.time_count(json.dumps({json})))""

    def set_up(self):
        self.search = views.search_place(json.dumps({"place": "bangkok"}))
        self.time = views.time_count(json.dumps({"origins\s": "bangkok", "destination": "pattaya"}))

    def test_sent_request(self):
        response = self.search
        self.assetNotContains(response,'200')
        
        response = self.search
        self.assetNotContains(response,'200')

    def test_remaining_time(self):

        self.assertEqual(json.dumps(17), remain_time(f'{{"duration" : "2",
        "remaining" : "22.30",
        "road" : "3 hours 30 mins"}}'))

        self.assertEqual(json.dumps(20.15), remain_time(f'{{"duration" : "1",
        "remaining" : "24",
        "road" : "2 hours 45 mins"}}'))

       self.assertEqual(json.dumps(22.40), remain_time(f'{{"duration" : "1",
       "remaining" : "24",
       "road" : "20 mins"}}'))

       self.assertEqual(json.dumps(3), remain_time(f'{{"duration" : "1",
       "remaining" : "24",
       "road" : "2 hours"}}'))

       self.assertEqual(json.dumps(17.4), remain_time(f'{{"duration" : "1",
       "remaining" : "20.4",
       "road" : "2 hours"}}'))

class Test_ptime(TestCase):

    def test_is_int(self):     
        self.assertTrue(ptime.is_int("3"))
        self.assertFalse(ptime.is_int("int"))

    def test_int_time(self):
        self.assertEqual(2.30, "2 hours 30 mins")
        self.assertEqual(4, "4 hours")
        self.assertEqual(0.45, "45 mins")
        self.assertEqual(0.03, "3 mins")
        self.assertEqual(0, "is int")
        self.assertEqual(0, "")    




