#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 00:16:11 2019

@author: wumeiqi
"""

#%% Information of appliccant
YOB = 1997
Income = 1000
address='Cornell University, USA'
Apl_Year = 2019
gender = 0

#%% Import packages
import urllib3, requests, json
import urllib.request, urllib.parse, urllib.error
import json
import ssl
import json


#%% Using google place API to extract the longitude and lagitude of address
def get_LonLat(address):
    # ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode =ssl.CERT_NONE
    
    api_key = ''
    serviceurl = 'https://maps.googleapis.com/maps/api/place/textsearch/json?'
  #  address='Cornell University, USA'
    
    parms = dict()
    parms['query'] = address
    parms['key'] = api_key
    url = serviceurl+urllib.parse.urlencode(parms)
    
#    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode() #### data is a string
#    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))
    
    try:
        js = json.loads(data) #### js is a dict
    except:
        print(data) # print in case unicode causes an error
        
    if 'status' not in js or (js['status']!='OK' and js['status']!='ZERO_RESULTS'):
        print('==== Failure To Retrieve ====')
        print(data)
    
    js = json.loads(str(data))
    lon = js['results'][0]['geometry']['location']['lng']
    lat = js['results'][0]['geometry']['location']['lat']
#    print('Longitude : ', lon)
#    print('Latitude : ', lat)
    return([lon, lat])
#%% 

apikey= "5QvD8hAoDtldp0mUvQ7EyrYqUCEvgb-grBeH2a4RM_Hc"
    
# Request iam_token
url     = "https://iam.bluemix.net/oidc/token"
headers = { "Content-Type" : "application/x-www-form-urlencoded" }
data    = "apikey=" + apikey + "&grant_type=urn:ibm:params:oauth:grant-type:apikey"
IBM_cloud_IAM_uid = "bx"
IBM_cloud_IAM_pwd = "bx"
response  = requests.post( url, headers=headers, data=data, auth=( IBM_cloud_IAM_uid, IBM_cloud_IAM_pwd ) )
iam_token = response.json()["access_token"]

# instance_id
ml_instance_id = "9d0fcc7a-39a9-4874-a1fb-cdc5df9b3901"


# Type in the values to be scored here: 
# ["YOB", "Income", "Lon", "Lat", "Lon_lat", "Apl_Year", "gender"]
location = get_LonLat(address)
array_of_values_to_be_scored = [YOB, Income, location[0], location[1], 
                                str(location[0])+', '+str(location[1]), Apl_Year, gender]

    
# NOTE: generate iam_token and retrieve ml_instance_id based on provided documentation
header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + iam_token, 'ML-Instance-ID': ml_instance_id}
    
# NOTE: manually define and pass the array(s) of values to be scored in the next line
#payload_scoring = {"input_data": [{"fields": ["YOB", "Income", "Lon", "Lat", "Lon_lat", "Apl_Year", "gender"], 
#                                   "values": [array_of_values_to_be_scored, another_array_of_values_to_be_scored]}]}
payload_scoring = {"input_data": [{"fields": ["YOB", "Income", "Lon", "Lat", "Lon_lat", "Apl_Year", "gender"], 
                                   "values": [array_of_values_to_be_scored]}]}
    
    
response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/v4/deployments/700e82e2-463e-4c2d-90fe-44acf4a2fbf6/predictions', 
                                 json=payload_scoring, headers=header)
print("Scoring response")
scoring = json.loads(response_scoring.text)
print('The possibility of acceptance is: ')
print(scoring['predictions'][0]['values'][0][1][1])
