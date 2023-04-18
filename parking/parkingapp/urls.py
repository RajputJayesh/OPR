from django.urls import path
from parkingapp import views

urlpatterns = [

    path('about',views.about),
    path('base',views.base),
    path('',views.index),
    path('home',views.home),
    path('service',views.services),
    path('price',views.pricing),
    path('contact',views.contact),
    path('add',views.Addvehicle),
    path('exit',views.exitvehicle),
    path('exit/<rid>',views.edit),
    path('all_details',views.all_details),
    path('exit_all_details',views.exit_all_details),
    path('catfilter/<value>',views.catfilter),
    path('actfilter/<value>',views.actfilter),
    path('register',views.user_register),
    path('login',views.user_login),
    path('reg',views.user_msg),
    path('logout',views.user_logout),
    

]