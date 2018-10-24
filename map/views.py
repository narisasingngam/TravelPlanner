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

# def test_database(request):
#     location = Location.objects.all()
#     for i in location:
#         print(i)
