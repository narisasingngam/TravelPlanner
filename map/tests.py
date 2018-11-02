from django.test import TestCase
from views.py import .
import json

class TestMethodsInViews(TestCase):

    def set_up(self):
        self.search = views.search_place(json.dumps{"place": "bangkok"})
        self.time = views.time_count(json.dumps{"origins\s": "bangkok", "destination": "pattaya"})

    def test_sent_request(self):
        response = self.search
        self.assetNotContains(response,'200')
        

