from django.test import TestCase
# from views.py import .
# import json
from map.models import Planner,Users

class PlannerModelTests(TestCase):

    def setUp(self):
        """
        Set up data 
        """
        Planner.objects.create(location = "CentralWorld",stay_time = 1,times = "11:30",date = "10/2/18")
        Planner.objects.create(location = "SiamDiscovery",stay_time = 2,times = "12:30",date = "11/2/18")
        Planner.objects.create(location = "Kasetsart University",stay_time = 3,times = "15:30",date = "12/2/18")
        test_plan_user = Planner.objects.create(location = "CentralWorld",stay_time = 1,times = "11:30",date = "10/2/18")
        Users.objects.create(email= "mmintttt@gmail.com",plans= test_plan_user)
    
    def test_Planner_name(self):
        """
        test name location 
        """
        plan = Planner.objects.all()
        self.assertEqual(plan[0].location, "CentralWorld")
        self.assertEqual(plan[1].location, "SiamDiscovery")
        self.assertEqual(plan[2].location, "Kasetsart University")
    
    def test_Planner_stay_time(self):
        """
        test stay time in Planner object  
        """
        stay = Planner.objects.all()

        self.assertEqual(stay[0].stay_time,1)
        self.assertEqual(stay[1].stay_time,2)
        self.assertEqual(stay[2].stay_time,3)
    
    def test_Planner_times(self):
        """
        test time table in Planner object  
        """
        time = Planner.objects.all()

        self.assertEqual(time[0].times,"11:30")
        self.assertEqual(time[1].times,"12:30")
        self.assertEqual(time[2].times,"15:30")
    
    def test_Planner_date(self):
        """
        test date in Planner object  
        """
        date = Planner.objects.all()

        self.assertEqual(date[0].date,"10/2/18")
        self.assertEqual(date[1].date,"11/2/18")
        self.assertEqual(date[2].date,"12/2/18")
    
    def test_Users_email(self):
        """
        test email in Users object  
        """
        user_email = Users.objects.all()

        self.assertEqual(user_email[0].email,"mmintttt@gmail.com")
    
    def test_User_plan(self):
        """
        test ForeignKey plan in Users object  
        """
        user_plan = Users.objects.all()
        self.assertEqual(user_plan[0].plans.location,"CentralWorld")
        self.assertEqual(user_plan[0].plans.stay_time,1)
        self.assertEqual(user_plan[0].plans.times,"11:30")
        self.assertEqual(user_plan[0].plans.date,"10/2/18")
