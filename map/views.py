from django.shortcuts import render
from .models import Location,User

def index(request):
    if request.method == 'POST':
          if request.POST.get('location') and request.POST.get('stay_time'):
                post= Location()
                post.location= request.POST.get('location')
                post.stay_time= request.POST.get('stay_time')
                post.save()
                
                return render(request, 'index.html')  
    else:
        return render(request,'index.html')

def test_database(request):
    location = Location.objects.all()
    user_planner = []
    user = User.objects.filter(email='mmintttt@gmail.com')

    for i in location:
        for j in user:
            if(i.user_id == j.id):
                print(Location.objects.filter(location = i.location,user_id = i.user_id,time = i.time))

    for i in user:
        print(i)