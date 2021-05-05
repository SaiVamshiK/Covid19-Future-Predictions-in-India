from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='Home-Page'),
    path('about/',views.about,name='About-Page'),
    path('display_plot/',views.display_plot,name='Display-Plot'),
    path('cumulative/',views.cumulative,name='Cumulative'),
    path('daywise/',views.daywise,name='Daywise'),
]
