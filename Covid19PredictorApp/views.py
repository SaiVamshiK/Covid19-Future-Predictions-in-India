import matplotlib.pyplot as plt
from django.shortcuts import render
from django.http import HttpResponse
from matplotlib.backends.backend_agg import FigureCanvasAgg
import pandas as pd
import datetime
from io import StringIO
import numpy as np
import io
import os
# Create your views here.

states = [
    {
        'image' : '../../../static/Covid19PredictorApp/state_images/tamilnadu.png',
        'name' : 'Tamil Nadu'
    },
    {
        'image' : '../../../static/Covid19PredictorApp/state_images/bihar.png',
        'name' : 'Bihar'
    },
    {
        'image' : '../../../static/Covid19PredictorApp/state_images/gujarat.png',
        'name' : 'Gujarat'
    },
    

    {
        'image' : '../../../static/Covid19PredictorApp/state_images/andhrapradesh.png',
        'name' : 'Andhra Pradesh'
    },
    {
        'image' : '../../../static/Covid19PredictorApp/state_images/telangana.png',
        'name' : 'Telangana'
    },
    
    {
        'image' : '../../../static/Covid19PredictorApp/state_images/arunachalpradesh.png',
        'name' : 'Arunachal Pradesh'
    },
    {
        'image' : '../../../static/Covid19PredictorApp/state_images/himachalpradesh.png',
        'name' : 'Himachal Pradesh'
    },

    {
        'image' : '../../../static/Covid19PredictorApp/state_images/jammuandkashmir.png',
        'name' : 'Jammu and Kashmir'
    },
    {
        'image' : '../../../static/Covid19PredictorApp/state_images/madhyapradesh.png',
        'name' : 'Madhya Pradesh'
    },
    {
        'image' : '../../../static/Covid19PredictorApp/state_images/maharashtra.png',
        'name' : 'Maharashtra'
    },
    {
        'image' : '../../../static/Covid19PredictorApp/state_images/jharkhand.png',
        'name' : 'Jharkhand'
    },
    {
        'image' : '../../../static/Covid19PredictorApp/state_images/karnataka.png',
        'name' : 'Karnataka'
    },
    {
        'image' : '../../../static/Covid19PredictorApp/state_images/kerala.png',
        'name' : 'Kerala'
    },
    {
        'image' : '../../../static/Covid19PredictorApp/state_images/assam.png',
        'name' : 'Assam'
    },
    {
        'image' : '../../../static/Covid19PredictorApp/state_images/chandigarh.png',
        'name' : 'Chandigarh'
    },
    {
        'image' : '../../../static/Covid19PredictorApp/state_images/chhattisgarh.png',
        'name' : 'Chhattisgarh'
    },
    {
        'image' : '../../../static/Covid19PredictorApp/state_images/delhi.png',
        'name' : 'Delhi'
    },

    {
        'image' : '../../../static/Covid19PredictorApp/state_images/tripura.png',
        'name' : 'Tripura'
    },
    {
        'image' : '../../../static/Covid19PredictorApp/state_images/uttarakhand.png',
        'name' : 'Uttarakhand'
    },
    {
        'image' : '../../../static/Covid19PredictorApp/state_images/uttarpradesh.png',
        'name' : 'Uttar Pradesh'
    },
    {
        'image' : '../../../static/Covid19PredictorApp/state_images/goa.png',
        'name' : 'Goa'
    },
    {
        'image' : '../../../static/Covid19PredictorApp/state_images/andamanandnicobarislands.png',
        'name' : 'Andaman and Nicobar Islands'
    },
    {
        'image' : '../../../static/Covid19PredictorApp/state_images/haryana.png',
        'name' : 'Haryana'
    },
    
    
    {
        'image' : '../../../static/Covid19PredictorApp/state_images/ladakh.png',
        'name' : 'Ladakh'
    },
    
    {
        'image' : '../../../static/Covid19PredictorApp/state_images/manipur.png',
        'name' : 'Manipur'
    },
    {
        'image' : '../../../static/Covid19PredictorApp/state_images/meghalaya.png',
        'name' : 'Meghalaya'
    },
    {
        'image' : '../../../static/Covid19PredictorApp/state_images/mizoram.png',
        'name' : 'Mizoram'
    },
    {
        'image' : '../../../static/Covid19PredictorApp/state_images/nagaland.png',
        'name' : 'Nagaland'
    },
    {
        'image' : '../../../static/Covid19PredictorApp/state_images/odisha.png',
        'name' : 'Odisha'
    },
    {
        'image' : '../../../static/Covid19PredictorApp/state_images/punjab.png',
        'name' : 'Punjab'
    },
    {
        'image' : '../../../static/Covid19PredictorApp/state_images/rajasthan.png',
        'name' : 'Rajasthan'
    },

    {
        'image' : '../../../static/Covid19PredictorApp/state_images/sikkim.png',
        'name' : 'Sikkim'
    },
    
    {
        'image' : '../../../static/Covid19PredictorApp/state_images/westbengal.png',
        'name' : 'West Bengal'
    }


    

]
    


def home(request):
    context = {
        'states' : states
    }
    return render(request,'Covid19PredictorApp/home.html',context)

def about(request):
    return render(request,'Covid19PredictorApp/about.html')


def display_plot(request):
    if 'state_name' in request.GET:
        message = request.GET['state_name']
    else:
        message = 'No state selected!!'

    context = {
        'state_name' : message
    }

    return render(request,'Covid19PredictorApp/display_plot.html',context)

def cumulative(request):
    if 'state_name' in request.GET:
        message = request.GET['state_name']
    else:
        message = 'No state selected!!'

    context = {
        'state_name' : message
    }
    df = pd.read_csv("https://api.covid19india.org/csv/latest/states.csv")
    dates = []
    confirmed_cases = []
    for i in range(len(df)):
        if df.iloc[i]['State'] == message:
            t = df.iloc[i]['Date'].split('-')
            v = datetime.datetime(int(t[0]),int(t[1]),int(t[2]))
            dates.append(v)
            confirmed_cases.append(df.iloc[i]['Confirmed'])

    fig, ax = plt.subplots()
    ax.plot(dates, confirmed_cases)
    ax.grid()
    stri = "Confirmed cases in "+message
    plt.title(stri)
    plt.xlabel("Dates")
    plt.ylabel("Confirmed cases")
    buf = io.BytesIO()
    plt.savefig(buf,format='png')
    plt.close(fig)
    response = HttpResponse(buf.getvalue(),content_type='image/png')
    return response


def daywise(request):
    if 'state_name' in request.GET:
        message = request.GET['state_name']
    else:
        message = 'No state selected!!'

    context = {
        'state_name' : message
    }
    df = pd.read_csv("https://api.covid19india.org/csv/latest/states.csv")
    dates = []
    confirmed_cases = []
    for i in range(len(df)):
        if df.iloc[i]['State'] == message:
            t = df.iloc[i]['Date'].split('-')
            v = datetime.datetime(int(t[0]),int(t[1]),int(t[2]))
            dates.append(v)
            confirmed_cases.append(df.iloc[i]['Confirmed'])
    day_wise = []
    day_wise.append(confirmed_cases[0])

    for i in range(1,len(confirmed_cases)):
        day_wise.append(confirmed_cases[i]-confirmed_cases[i-1])
    fig2, ax = plt.subplots()
    ax.plot(dates, day_wise)
    ax.grid()
    stri = "Daywise new cases in "+message
    plt.title(stri)
    plt.xlabel("Dates")
    plt.ylabel("New cases")
    buf = io.BytesIO()
    plt.savefig(buf,format='png')
    plt.close(fig2)
    response = HttpResponse(buf.getvalue(),content_type='image/png')
    return response
    
    

    

    

    


