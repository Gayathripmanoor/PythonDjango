from django.http import HttpResponse
from django.shortcuts import render
from . models import places
from . models import Meet
# Create your views here.
def demo(request):
     obj = places.objects.all()
     objts = Meet.objects.all()
     return render(request, 'index.html', {'result': obj,'results':objts})

# def meet(request):
#      objts = Meet.objects.all()
#      return render(request, 'index.html', {'result': objts})
#

# def demo(request):

    # return render (request,'index.html',{'results':obj})