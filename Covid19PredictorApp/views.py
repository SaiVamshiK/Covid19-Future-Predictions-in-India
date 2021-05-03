from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

states = [
    {
        'image' : '../../../static/Covid19PredictorApp/state_images/tamilnadu.png',
        'name' : 'Tamilnadu'
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


