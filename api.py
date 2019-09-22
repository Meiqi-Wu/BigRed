#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 00:16:11 2019

@author: wumeiqi
"""

import urllib3, requests, json

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
array_of_values_to_be_scored = [1997, 1000, 46, 46, "46, 23", 2018, 0]

    
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
