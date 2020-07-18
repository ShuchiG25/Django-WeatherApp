# from django.shortcuts import render
#
# # Create your views here.
# def index(request):
#     return render(request,'weather.html')
from django.contrib import messages
from django.contrib.sites import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
# import json to load json data to python dictionary
import json
# urllib.request to make a request to api
import urllib.request

#  from geeks of geekss
def index(request):
 #   print("**************inside index method ...........request.method..."- request.method())
    if request.method == 'POST':
        city = request.POST['city']
        # source contain JSON data from API
        print("city............... - ", city)
        try:
             source = urllib.request.urlopen(
            "http://api.openweathermap.org/data/2.5/weather?q=" + city +
            "your API code").read()
        except urllib.error.HTTPError as e:
             print('HTTPError: {}'.format(e.code))
             data = {}
             print ("inside try except - if invalid city - data - ", data)
             messages.info(request, 'Invalid city name, Please check the spelling !!')
             return redirect("/")

        else:
            print("inside try else..................if valid city ")

            # converting JSON data to a dictionary
            list_of_data = json.loads(source)
            print("*************************************- ", list_of_data)
            # data for variable list_of_data
            data = {
                "city_name": str(list_of_data['name']),
                "country_code": str(list_of_data['sys']['country']),
                "coordinate": str(list_of_data['coord']['lon']) + ' '
                              + str(list_of_data['coord']['lat']),
                "temp": str("{:.2f}".format((list_of_data['main']['temp'])- int(273))) + ' C',
                "pressure": str(list_of_data['main']['pressure']),
                "humidity": str(list_of_data['main']['humidity']),
            }
            print(data)

    else:
            print("inside main if else.........")
            data = {}
            print("................data - ", data)
            print("................data - ", len(data))



    return render(request, "index.html", data)

