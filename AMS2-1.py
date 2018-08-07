import requests
import json
import re

user_agent='Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/29.0'
headers={'User-Agent': user_agent,
'X-Auth-Token': 'a9tn1u3hrnb4l3scp6v682g68t',
    	'Content-type': 'application/json',
	'Accept': 'application/json'} 

url="http://api-v2.applymagicsauce.com/like_ids"

###############################
##### OPEN THE PEOPLE FILE ####
###############################
res=[]
with open("people.txt","r") as f:
	sentences = [elem for elem in f.read().split('\n') if elem]
	for sentence in sentences:
		res.append(sentence.split(','))

for k in range(0,len(res)):
	res[k][1] = re.sub(r'[^\w]','',res[k][1])
	
###############################
##### OPEN THE LIKES' FILE ####
###############################
with open("Tdata.json") as json_file:
    json_data = json.load(json_file)


###############################
##### ACCESSING AMS API #######
###############################
for k in range(0,len(res)):
	payload = []
	for i in range(0,100):
		i = str(i)
		j = res[k][1]
		addThis = json_data[j][i]
		payload.append(addThis)
	params ={'traits': 'BIG5_Neuroticism,BIG5_Conscientiousness,BIG5_Openness,BIG5_Agreeableness,BIG5_Extraversion', 'uid': res[k][1]}
	r = requests.post(url,params=params ,data=json.dumps(payload), headers=headers)
	print res[k][0]
	print r
	print r.text
