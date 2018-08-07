import requests
import json

user_agent='Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/29.0'
headers={'User-Agent': user_agent,
    	'Content-type': 'application/json',
	'Accept': 'application/json'} 

url="http://api-v2.applymagicsauce.com/auth"
payload = {'customer_id':'292','api_key':'p1temdbgvgs6667clkscaivjob'}

r = requests.post(url,data=json.dumps(payload), headers=headers)

A = r.json()
token =  A['token']

print token