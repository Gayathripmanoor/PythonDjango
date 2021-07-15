from . import views
from django.urls import path, include

urlpatterns = [

    path('',views.demo,name='demo'),


    #path('calc/',views.calculation,name='calculation'),
    #path('sub/',views.calculation,name='subtraction'),
    #path('mul/',views.calculation,name='multiplication'),
    #path('div/',views.calculation,name='division'),

    #path('about/',views.about,name='about'),
    #path('contact',views.contact,name='contact'),
    #path('details/',views.details,name='details'),
    #path('thanks/',views.thanks,name='thanks'),
]
