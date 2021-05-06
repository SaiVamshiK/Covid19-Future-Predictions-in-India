from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='Home-Page'),
    path('about/',views.about,name='About-Page'),
    path('see_prediction/',views.see_prediction,name='See-Prediction'),
    path('cumulative/',views.cumulative,name='Cumulative'),
    path('daywise/',views.daywise,name='Daywise'),
    path('overall/',views.overall,name='Overall-Analysis'),
    path('overall/display_plot/',views.overallDisplay,name='Display-Overall-Analysis'),
    path('overall/cumulative/',views.overallCumulative,name='Cumulative-Overall-Analysis'),
    path('overall/daywise/',views.overallDaywise,name='Daywise-Overall-Analysis'),
]
