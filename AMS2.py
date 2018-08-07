import requests
import json

user_agent='Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/29.0'
headers={'User-Agent': user_agent,
'X-Auth-Token': 'ulopdaihhekn7irs5el2iunfhd',
    	'Content-type': 'application/json',
	'Accept': 'application/json'} 

url="http://api-v2.applymagicsauce.com/like_ids"

###############################
##### OPEN THE LIKES FILE #####
###############################
res=[]
with open("people.txt","r") as f:
	sentences = [elem for elem in f.read().split('\n') if elem]
	for sentence in sentences:
		res.append(sentence.split(','))


with open("Tdata.json") as json_file:
    json_data = json.load(json_file)

#print json_data['1135086359']

for k in range(0,len(res)):
	payload = []
	for i in range(0,100):
		i = str(i)
		payload.append(json_data[res[k][1]][i])
	params ={'traits': 'BIG5_Neuroticism,BIG5_Conscientiousness,BIG5_Openness,BIG5_Agreeableness,BIG5_Extraversion', 'uid': res[k][1]}
	r = requests.post(url,params=params ,data=json.dumps(payload), headers=headers)
	print r.text


# payload = []

# #params ={'traits': 'BIG5_Neuroticism,BIG5_Conscientiousness,BIG5_Openness,BIG5_Agreeableness,BIG5_Extraversion', 'uid': '525768181'}


# params ={'traits': 'age', 'uid': '525768181'}

# r = requests.post(url,params=params ,data=json.dumps(payload), headers=headers)
# print r
# print r.text
