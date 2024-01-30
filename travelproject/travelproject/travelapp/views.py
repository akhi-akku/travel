from django.http import HttpResponse
from django.shortcuts import render
from .models import places
from .models import People

# Create your views here.
def demo(request):
    obj=places.objects.all()
    obj1=People.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})


#def contact(request):
#    return HttpResponse("I am Contact Page")
