from django.http import HttpResponse
from django.shortcuts import render
from . models import places
# Create your views here.
def demo(request):
    obj=places.objects.all()
    return render(request,'index.html',{'result':obj})

#def calculation(request):

#    x=int(request.GET['num1'])
#    y=int(request.GET['num2'])
#    add=x+y
 #   sub=x-y
 #   mul=x*y
 #   div=x/y
    #return render(request,'result.html',{'x':add , 'y':sub, 'z':mul, 'w':div})
#def subtraction(request):

 # x=int(request.GET['num1'])
  #y=int(request.GET['num2'])
  #sub=x-y
  #return render(request,'result.html',{'result':sub})
#def multiplication(request):

 #   x=int(request.GET['num1'])
  #  y= int(request.GET['num2'])
   # mul=x*y
  #  return render(request,'result.html',{'result':mul})
#def division(request):

 #  x=int(request.GET['num1'])
  # y=int(request.GET['num2'])
   #div=x/y
   #return render(request,'result.html',{'result':div})
#def about(request):
#    return render(request,'about.html')

#def contact(request):
 #   return HttpResponse('HI ALL YOU CAN CONTACT US ANYTIME')

#def details(request):
 #   return render(request,'details.html')

#def thanks(request):
 #   return HttpResponse('THANK YOU FOR VISITING')
