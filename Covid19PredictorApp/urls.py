from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='Home-Page'),
    path('about/',views.about,name='About-Page'),
    path('see_prediction/',views.see_prediction,name='See-Prediction'),
    path('cumulative/',views.cumulative,name='Cumulative'),
    path('daywise/',views.daywise,name='Daywise'),
]
