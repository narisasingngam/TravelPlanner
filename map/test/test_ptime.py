from django.test import TestCase
from map import ptime

class Test_ptime(TestCase):

    def test_is_int(self):  
        '''
        test for checking int.
        '''  
        self.assertTrue(ptime.is_int("3"))
        self.assertFalse(ptime.is_int("int"))

    def test_int_time(self):
        '''
        test parsing time from string to int.
        '''
        self.assertEqual(2.30,ptime.int_time("2 hours 30 mins"))
        self.assertEqual(4,ptime.int_time("4 hours"))
        self.assertEqual(0.45,ptime.int_time("45 mins"))
        self.assertEqual(0.03,ptime.int_time("3 mins"))
        self.assertEqual(0,ptime.int_time("is int"))
        self.assertEqual(0,ptime.int_time(""))