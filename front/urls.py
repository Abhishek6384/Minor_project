from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='indexpage'),
    path('home',views.index,name='indexpage'),
    path('login',views.loginPage,name='login'),
    path('signup',views.signup,name='signup'),
    path('logout/',views.logoutUser,name='logout'),
    path('contact',views.contact,name='contact'),
    path('save',views.save,name='saveform'),
    path('prevresult',views.all_results,name='allresult')
   
   
]
