from . import views
from django.urls import path,include

urlpatterns = [

    path('',views.demo,name='demo'),
    #path('add/',views.addition,name='about'),
    #path('contact/',views.contact,name='contact'),
]
