from django.test import TestCase
from django.test import Client
from django.urls import reverse
from map.models import Planner,Users
import json

class PlannerModelTests(TestCase):

    def setUp(self):
        """
        Set up data 
        """
        Planner.objects.create(location = "CentralWorld",spend_time = 1,times = "11:30",date = "10/2/18",duration="3 hours",name_planner="trip",id_plan='01',total_time='11:30')
        Planner.objects.create(location = "SiamDiscovery",spend_time = 2,times = "12:30",date = "11/2/18",duration="2 hours",name_planner="trip",id_plan='02',total_time='13:30')
        Planner.objects.create(location = "Kasetsart University",spend_time = 3,times = "15:30",date = "12/2/18",duration="1 hour",name_planner="trip",id_plan='03',total_time='15:30')
        
        user_date1_plan = Planner.objects.create(location = "SiamDiscovery",spend_time = 2,times = "12:30",date = "11/2/18",duration="2 hours",name_planner="trip",id_plan='02',total_time='13:30')
        user_date2_plan = Planner.objects.create(location = "Kasetsart University",spend_time = 3,times = "15:30",date = "10/2/18",duration="1 hour",name_planner="trip",id_plan='03',total_time='15:30')
        user_date3_plan = Planner.objects.create(location = "CentralWorld",spend_time = 1,times = "11:30",date = "10/2/18",duration="3 hours",name_planner="trip",id_plan='01',total_time='11:30')

        Users.objects.create(email= "mmintttt@gmail.com",plans= user_date3_plan)
        Users.objects.create(email= "mmintttt@gmail.com",plans= user_date2_plan)
        Users.objects.create(email= "mmintttt@gmail.com",plans= user_date1_plan)
    
    def test_Planner_name(self):
        """
        test name location 
        """
        plan = Planner.objects.all()
        self.assertEqual(plan[0].location, "CentralWorld")
        self.assertEqual(plan[1].location, "SiamDiscovery")
        self.assertEqual(plan[2].location, "Kasetsart University")
    
    def test_Planner_spend_time(self):
        """
        test stay time in Planner object  
        """
        stay = Planner.objects.all()

        self.assertEqual(stay[0].spend_time,"1")
        self.assertEqual(stay[1].spend_time,"2")
        self.assertEqual(stay[2].spend_time,"3")
    
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
        plan = Planner.objects.all()

        self.assertEqual(user_plan[0].plans.location,plan[0].location)
        self.assertEqual(user_plan[0].plans.spend_time,plan[0].spend_time)
        self.assertEqual(user_plan[0].plans.times,plan[0].times)
        self.assertEqual(user_plan[0].plans.date,plan[0].date)

    def test_user_data(self):
        '''
        test list user data
        '''
        c = Client()
        data = {"email" : "mmintttt@gmail.com"}
        response = c.post(reverse('travelplanner:user'),data,content_type="application/json")
        result = response.content
        list = [{'date': '10/2/18', 'id': '01', 'name': 'trip'},{'date': '10/2/18', 'id': '03', 'name': 'trip'},{'date': '11/2/18', 'id': '02', 'name': 'trip'}]
        self.assertEquals(json.loads(result), list)

    def test_type_error(self):
        '''
        test type error location and date always be string
        '''
        plan = Planner.objects.create(location = 234 ,spend_time = 2,times = "12:30",date = 11/2/18 ,duration="2 hours",name_planner="trip",id_plan='03',total_time='22.30')
        self.assertRaises(TypeError,plan)
