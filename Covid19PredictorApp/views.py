import matplotlib.pyplot as plt
from django.shortcuts import render
from django.http import HttpResponse
from matplotlib.backends.backend_agg import FigureCanvasAgg
import pandas as pd
import datetime
from datetime import date, timedelta
from io import StringIO
import numpy as np
import io
import os
import math
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model
from sklearn.metrics import mean_absolute_error
from sklearn.linear_model import LinearRegression
# Create your views here.
from datetime import date, timedelta
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
    },
    {
        'image' : '../../../static/Covid19PredictorApp/state_images/india.png',
        'name' : 'India'
    }
    

]
    


def home(request):
    context = {
        'states' : states
    }
    return render(request,'Covid19PredictorApp/home.html',context)

def about(request):
    return render(request,'Covid19PredictorApp/about.html')


def see_prediction(request):
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
    X = [x for x in range(1,len(dates)+1)]
    poly = PolynomialFeatures(degree=8)
    new_X = poly.fit_transform(np.array(X).reshape(-1,1))
    LR = LinearRegression()
    model = LR.fit(new_X,confirmed_cases)

    fromm = len(confirmed_cases)-10
    upto = len(confirmed_cases)+10

    nums = np.arange(1,upto).reshape(-1,1)
    poly  = PolynomialFeatures(degree=8)
    inp_X = poly.fit_transform(nums)
    predictions = model.predict(inp_X)

    actual_cases = []
    predicted_cases = []
    days_before = date.today()-timedelta(days=10)
    dates = []
    for i in range(fromm,upto-1):
        if(i<len(confirmed_cases)):
            actual_cases.append(confirmed_cases[i])
            predicted_cases.append(math.floor(predictions[i]))
        else:
            predicted_cases.append(math.floor(predictions[i]))
        dates.append(days_before)
        days_before = days_before+timedelta(days=1)
    
    context['actual_cases'] = actual_cases
    context['predicted_cases'] = predicted_cases
    context['length'] = len(confirmed_cases)
    context['Date'] = dates
    return render(request,'Covid19PredictorApp/see_prediction.html',context)

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
    
    

def overall(request):
    df = pd.read_csv("https://api.covid19india.org/csv/latest/states.csv")
    dates = []
    confirmed_cases = []
    for i in range(len(df)):
        if df.iloc[i]['State'] == 'India':
            t = df.iloc[i]['Date'].split('-')
            v = datetime.datetime(int(t[0]), int(t[1]), int(t[2]))
            dates.append(v)
            confirmed_cases.append(df.iloc[i]['Confirmed'])
    X = [x for x in range(1, len(dates) + 1)]
    poly = PolynomialFeatures(degree=8)
    new_X = poly.fit_transform(np.array(X).reshape(-1, 1))
    LR = LinearRegression()
    model = LR.fit(new_X, confirmed_cases)

    confirmed_india = []
    dates_india = []
    for i in range(len(df)):
        if (df.iloc[i]['State'] == "India"):
            confirmed_india.append(df.iloc[i]['Confirmed'])
            dates_india.append(df.iloc[i]['Date'])
    for i in range(len(confirmed_india)):
        print(dates_india[i], confirmed_india[i])



    context = {
        'states': states
    }
    import math
    nums = np.arange(1, 2000).reshape(-1, 1)
    poly = PolynomialFeatures(degree=8)
    inp_X = poly.fit_transform(nums)
    predictions = model.predict(inp_X)

    plt.figure(figsize=(19, 8))
    print(len(nums))
    print(len(predictions))
    exp_date = 0
    change = False
    for i in range(400, 1999):
        temp = predictions[i] - predictions[i - 1]
        print(math.floor(predictions[i] - predictions[i - 1]))
        if (temp < 0):
            if change == False:
                exp_date = i - 1
                change = True
    num_days = exp_date - len(confirmed_india)

    current_date = date.today().isoformat()
    days_after = (date.today() + timedelta(days=num_days)).isoformat()
    context['current-date']=current_date
    context['deadline']=days_after

    return render(request,'Covid19PredictorApp/overall.html',context)
    
