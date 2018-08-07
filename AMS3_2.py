import facebook
import json
from collections import Counter

#your access token, use version 1 API for friends data
ACCESS_TOKEN='CAACEdEose0cBAHsqhFtIcEjg2iDQnRaelaUj1IoZBqwaSPfNtTfZCoIgYEcH78np1gzCHs2VaZBhfPw5nL1WHTLwfewZBNi2C2QrznoBeZAKy7PQZCSv0hSpywUJG81p0jZAUFpnRU0jLjYM5Tanh0YauUBXhAnL6GSSVJnScYYtkiNbqZCSXwkJSAYxITOuuZAfmchHR8kEZAZAtX4ywh5Tj5MqBgkDOVpSHUZD'
g=facebook.GraphAPI(ACCESS_TOKEN)

friends = g.get_object('me/friends')

#Change this survey takers list. With the following people : Madhulika Mukherjee
surveytakers = ['Madhulika Mukherjee']

surveytakers = sorted(surveytakers)

list_of_id = []
likes = []
for person in surveytakers:
	for friend in friends['data']:
		#That extra friend ID is for Prashant Sinha
		if friend['name'] == person or friend['id'] == '100000509019671':
			list_of_id.append(friend['id'])
			likes.append ({ friend['name'] : g.get_connections(friend['id'], "likes", limit=150)['data'] })

#binding the surveytakers with their UIDs
surveytakers.append('Prashant Sinha')
people = zip(surveytakers, list_of_id)
print people

#Making the json readable
with open('likes.json','w') as outfile:
	json.dump(likes, outfile, indent=4)


json_decoded = json.dumps(likes, indent=4)
data = json.loads(json_decoded)

#sorting and putting it back into the file
data = sorted(data)
with open('likes.json','w') as outfile:
	json.dump(data, outfile, indent=4)

##################################
#### PARSING DATA INTO 'TDATA' ###
##################################

i = 0
Tdata = {}

for surveytaker in surveytakers:
	if surveytaker == people[i][0]:
		uid = people[i][1]
		tdict = {}
		print surveytaker
		for k in range(0,100):
			tdict[k] = data[i][surveytaker][k]['id']
		Tdata[uid] = dict()
		Tdata[uid].update(tdict)
		i = i+1

with open('Tdata.json','w') as outfile:
	json.dump(Tdata, outfile, indent=4)
