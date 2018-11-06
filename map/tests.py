from django.test import TestCase
from .models import Planner,Users

class PlannerModelTests(TestCase):

    def setUp(self):
        """
        Set up data 
        """
        Planner.objects.create(location = "CentralWorld",stay_time = 1,times = "11:30",date = "10/2/18")
        Planner.objects.create(location = "SiamDiscovery",stay_time = 2,times = "12:30",date = "11/2/18")
        Planner.objects.create(location = "Kasetsart University",stay_time = 3,times = "15:30",date = "12/2/18")
    
    def test_location_name(self):
        """
        test name location 
        """
        plan = Planner.objects.all()
        self.assertEqual(plan[0].location, "CentralWorld")
        self.assertEqual(plan[1].location, "SiamDiscovery")
        self.assertEqual(plan[2].location, "Kasetsart University")
    
    def test_location_stay_time(self):
        """
        test stay time in Planner object  
        """
        stay = Planner.objects.all()

        self.assertEqual(stay[0].stay_time,1)
        self.assertEqual(stay[1].stay_time,2)
        self.assertEqual(stay[2].stay_time,3)
        
    

