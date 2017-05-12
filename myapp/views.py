from django.shortcuts import render
from django.http import HttpResponseRedirect
import requests
from myapp.forms import CityLocForm, MyForm
import json
import requests


from django.shortcuts import render_to_response,RequestContext
from myapp.models import WeatherData
from myapp.forms import WeatherDataForm
from django.contrib.auth.decorators import login_required

from django import forms
from django.contrib.auth.forms import UserCreationForm


def index(request):
    weatherSearch = 'http://api.wunderground.com/api/f19317253942f8d6/satellite/conditions/q/' 
    manchester = 'http://api.wunderground.com/api/f19317253942f8d6/forecast10day/forecast/q/UK/Manchester.json'
    birmingham = 'http://api.wunderground.com/api/f19317253942f8d6/forecast10day/forecast/q/UK/Birmingham.json'
    liverpool = 'http://api.wunderground.com/api/f19317253942f8d6/forecast10day/forecast/q/UK/Liverpool.json' 	
    
    autoIp = 'http://api.wunderground.com/api/f19317253942f8d6/geolookup/q/autoip.json'

    	
    if request.method == 'POST':
        city_form = CityLocForm(request.POST)
        if city_form.is_valid():
            city = city_form.cleaned_data['city']
      
            request_url = weatherSearch + str(city) + '.json'

            r = requests.get(request_url)
            r = r.json
			
            request_url4 = autoIp
            ai = requests.get(request_url4)
            ai = ai.json
			
            request_url2 = manchester
            ma = requests.get(request_url2)
            ma = ma.json
			
            request_url3 = birmingham
            bi = requests.get(request_url3)
            bi = bi.json
			
            request_url4 = liverpool
            li = requests.get(request_url4)
            li = li.json
            try:
                weatherDesc = r['current_observation']['weather']
                weatherDescUrl = r['current_observation']['icon_url']

                weatherConditions = {'Temperature' : r['current_observation']['temperature_string'],
                                'Feels Like' : r['current_observation']['feelslike_string'],
                                'Dew Point' : r['current_observation']['dewpoint_string'],
                                'Relative Humidity' : r['current_observation']['relative_humidity'],
                                'Wind' : r['current_observation']['wind_string'],
                                'Windchill' : r['current_observation']['windchill_string'],
                                'Wind MPH' : r['current_observation']['wind_mph'],
                }
				
                location = r['current_observation']['observation_location']['full']
                searchmap = r['satellite']['image_url_ir4']
				
                weatherConditions1 = {'Latitude' : ai['location']['lat'],
                                'Longitude' : ai['location']['lon'],

                }
                location1 = ai['location']['city']
				
                #manchester
                maIcon0 =  ma['forecast']['simpleforecast']['forecastday'][0]['icon']
                maIconURL0 = ma['forecast']['simpleforecast']['forecastday'][0]['icon_url']
                
                getMaCondition1 = {'Day 1: ' : ma['forecast']['simpleforecast']['forecastday'][0]['date']['weekday'],
                                  'Low: ' : ma['forecast']['simpleforecast']['forecastday'][0]['low']['celsius'],
								  'High: ' : ma['forecast']['simpleforecast']['forecastday'][0]['high']['celsius'],
                }
                maIcon1 =  ma['forecast']['simpleforecast']['forecastday'][1]['icon']
                maIconURL1 = ma['forecast']['simpleforecast']['forecastday'][1]['icon_url']
                getMaCondition2 = {'Day 2: ' : ma['forecast']['simpleforecast']['forecastday'][1]['date']['weekday'],
                                  'Low: ' : ma['forecast']['simpleforecast']['forecastday'][1]['low']['celsius'],
								  'High: ' : ma['forecast']['simpleforecast']['forecastday'][1]['high']['celsius'],
                               
                }
                maIcon2 =  ma['forecast']['simpleforecast']['forecastday'][2]['icon']
                maIconURL2 = ma['forecast']['simpleforecast']['forecastday'][2]['icon_url']
                getMaCondition3 = {'Day 3: ' : ma['forecast']['simpleforecast']['forecastday'][2]['date']['weekday'],
                                  'Low: ' : ma['forecast']['simpleforecast']['forecastday'][2]['low']['celsius'],
								  'High: ' : ma['forecast']['simpleforecast']['forecastday'][2]['high']['celsius'],
                               
                }
				#birmingham
                biIcon0 =  bi['forecast']['simpleforecast']['forecastday'][0]['icon']
                biIconURL0 = bi['forecast']['simpleforecast']['forecastday'][0]['icon_url']
                
                getBiCondition1 = {'Day 1: ' : bi['forecast']['simpleforecast']['forecastday'][0]['date']['weekday'],
                                  'Low: ' : bi['forecast']['simpleforecast']['forecastday'][0]['low']['celsius'],
								  'High: ' : bi['forecast']['simpleforecast']['forecastday'][0]['high']['celsius'],
								  
                }
                biIcon1 =  bi['forecast']['simpleforecast']['forecastday'][1]['icon']
                biIconURL1 = bi['forecast']['simpleforecast']['forecastday'][1]['icon_url']
                getBiCondition2 = {'Day 2: ' : bi['forecast']['simpleforecast']['forecastday'][1]['date']['weekday'],
                                  'Low: ' : bi['forecast']['simpleforecast']['forecastday'][1]['low']['celsius'],
								  'High: ' : bi['forecast']['simpleforecast']['forecastday'][1]['high']['celsius'],
                               
                }
                biIcon2 =  bi['forecast']['simpleforecast']['forecastday'][2]['icon']
                biIconURL2 = bi['forecast']['simpleforecast']['forecastday'][2]['icon_url']
                getBiCondition3 = {'Day 3: ' : bi['forecast']['simpleforecast']['forecastday'][2]['date']['weekday'],
                                  'Low: ' : bi['forecast']['simpleforecast']['forecastday'][2]['low']['celsius'],
								  'High: ' : bi['forecast']['simpleforecast']['forecastday'][2]['high']['celsius'],
                               
                }
				
                #liverpool
                liIcon0 =  li['forecast']['simpleforecast']['forecastday'][0]['icon']
                liIconURL0 = li['forecast']['simpleforecast']['forecastday'][0]['icon_url']
                
                getLiCondition1 = {'Day 1: ' : li['forecast']['simpleforecast']['forecastday'][0]['date']['weekday'],
                                  'Low: ' : li['forecast']['simpleforecast']['forecastday'][0]['low']['celsius'],
                                  'High: ' : li['forecast']['simpleforecast']['forecastday'][0]['high']['celsius'],
								  
                }
                liIcon1 =  li['forecast']['simpleforecast']['forecastday'][1]['icon']
                liIconURL1 = li['forecast']['simpleforecast']['forecastday'][1]['icon_url']
                getLiCondition2 = {'Day 2: ' : li['forecast']['simpleforecast']['forecastday'][1]['date']['weekday'],
                                  'Low: ' : li['forecast']['simpleforecast']['forecastday'][1]['low']['celsius'],
                                  'High: ' : li['forecast']['simpleforecast']['forecastday'][1]['high']['celsius'],
                               
                }
                liIcon2 =  li['forecast']['simpleforecast']['forecastday'][2]['icon']
                liIconURL2 = li['forecast']['simpleforecast']['forecastday'][2]['icon_url']
                getLiCondition3 = {'Day 3: ' : li['forecast']['simpleforecast']['forecastday'][2]['date']['weekday'],
                                  'Low: ' : li['forecast']['simpleforecast']['forecastday'][2]['low']['celsius'],
                                  'High: ' : li['forecast']['simpleforecast']['forecastday'][2]['high']['celsius'],
                               
                }
                

                return render(request, 'index.html', {'location' : location,
                                                                    'location1' : location1,
                                                                    'getMaCondition1' : getMaCondition1,
                                                                    'getMaCondition2' : getMaCondition2,
                                                                    'getMaCondition3' : getMaCondition3,
																	'getBiCondition1' : getBiCondition1,
                                                                    'getBiCondition2' : getBiCondition2,
                                                                    'getBiCondition3' : getBiCondition3,
                                                                    'getLiCondition1' : getLiCondition1,
                                                                    'getLiCondition2' : getLiCondition2,
                                                                    'getLiCondition3' : getLiCondition3,
                                                                    'searchmap' : searchmap,
                                                                    'weatherConditions' : weatherConditions,
                                                                    'weatherConditions1' : weatherConditions1,
                                                                    'city_form' : city_form,
                                                                    'weatherDesc' : weatherDesc,
                                                                    'weatherDescUrl' : weatherDescUrl,
                                                                    'maIcon0' : maIcon0,
                                                                    'maIconURL0' : maIconURL0, 
                                                                    'maIcon1' : maIcon1,
                                                                    'maIconURL1' : maIconURL1,
                                                                    'maIcon1' : maIcon2,
                                                                    'maIconURL1' : maIconURL2, 
                                                                    'biIcon0' : biIcon0,
                                                                    'biIconURL0' : biIconURL0, 
                                                                    'biIcon1' : biIcon1,
                                                                    'biIconURL1' : biIconURL1,
                                                                    'biIcon2' : biIcon2,
                                                                    'biIconURL2' : biIconURL2,
                                                                    'liIcon0' : liIcon0,
                                                                    'liIconURL0' : liIconURL0, 
                                                                    'liIcon1' : liIcon1,
                                                                    'liIconURL1' : liIconURL1,
                                                                    'liIcon2' : liIcon2,
                                                                    'liIconURL2' : liIconURL2
                                                                    })
            except:
                error_msg = r['response']['error']['description']

                return render(request, 'index.html', {'city_form': city_form,
                                                                        'error_msg' : error_msg,
                                                                        })

    else:
        city_form = CityLocForm()

    return render(request, 'index.html', {'city_form': city_form,
                                                                    })
																	
																	

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/search-form/")
    else:
        form=UserCreationForm()

    return render(request,
                  "registration/register.html",
                  {'form':form})

def welcomeScreen(request):
    return render(request,'welcomeScreen.html')


@login_required
def search_form(request):
    print request.session
    return render(request,'search.html')


@login_required
def search(request):
    if 'q' in request.GET:
        term = request.GET['q']
    if not term:
        return render_to_response('search.html',{'error':True})
    data = WeatherData.objects.filter(city=term)
    if not data:
        return render(request,'search.html',{'error':True,'msg':'No match found for...'+term})

    return render(request,'searchOutput.html',{'term':term,'wdata':data})


@login_required
def weatherDataDisplay(request):
    form = WeatherDataForm()
    return render(request,
                  'weatherForm.html',
                  {'form':form})


@login_required
def weatherDataStore(request):
    if request.method == 'POST':
        form = WeatherDataForm(request.POST)

        if(form.is_valid()):
            cd = form.cleaned_data

            wd = WeatherData(city=cd['city'],
                             country=cd['country'],
                             timestamp=cd['date'],
                             temperature=cd['temperature'])
            wd.save()
            print("Saved weather record...")
        else:
            return render(request,
                          'weatherForm.html',{'form':form})

    print("calling update...")
    return render(request, 'update.html',{'term':"Saved data to d/base..."})

	
def my_view(request):
    form = MyForm()
   
    return render_response('index.html',{'form': form})