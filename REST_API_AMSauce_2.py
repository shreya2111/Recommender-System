import requests
import json

user_agent='Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/29.0'

headers={'User-Agent': user_agent,
	'Content-type': 'application/json',
	'Accept': 'application/json'} 

url="http://api-v2.applymagicsauce.com/auth"
payload = {'customer_id':'292','api_key':'p1temdbgvgs6667clkscaivjob'}
r = requests.post(url,data=json.dumps(payload), headers=headers)

A=r.json()
token=A['token']

print token

headers={'User-Agent': user_agent,
	'X-Auth-Token':token,
    	'Content-type': 'application/json',
	'Accept': 'application/json'} 

url="http://api-v2.applymagicsauce.com/like_ids"

payload=["139431019510816","120851194614115","309446385759638","17699655759","709783555706009","301297463250623",
"189691477731023","164615304283","53227312798","286369351555780","490759567612520","659323414162290","223018627846137","1718113051748108",
"120740541030","1591083317781566","137750259582504","1382930975283363","321872821251273","279518575468159","8075228697","108187262608717","112317682114594",
"108129905888537","206190329408695","139431019510816"]
   

params={'uid':'100007217470533','traits':'BIG5_Neuroticism,BIG5_Conscientiousness,BIG5_Openness,BIG5_Agreeableness,BIG5_Extraversion'}
r = requests.post(url,params=params,data=json.dumps(payload), headers=headers)
#token=r.json['token']

print r


