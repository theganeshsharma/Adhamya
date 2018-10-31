from . import views
from django.urls import path

app_name='homePage'

urlpatterns = [

    #home-page
    path('',views.index,name='index'),

    #login-page
    path('login/',views.user_login,name='login'),


    path('register/',views.registration,name='register'),



]