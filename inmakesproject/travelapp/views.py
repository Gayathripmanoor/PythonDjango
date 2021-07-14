from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from travelapp.models import Meet


def demo(request):
    obj=Meet.objects.all()
    return render (request,'index.html',{'result':obj})
#def addition(request):
  #  x=int(request.GET['num1'])
 #   y=int(request.GET['num2'])
   # res=x+y
    #return render(request,'result.html', {'result':res})
#def about(request):
#    return render(request,'about.html')

#def contact(request):
#    return render(request,'contact.html')