import facebook
import json
#from prettytable import PrettyTable
from collections import Counter

#your access token, use version 1 API for friends data
ACCESS_TOKEN='CAACEdEose0cBAHsqhFtIcEjg2iDQnRaelaUj1IoZBqwaSPfNtTfZCoIgYEcH78np1gzCHs2VaZBhfPw5nL1WHTLwfewZBNi2C2QrznoBeZAKy7PQZCSv0hSpywUJG81p0jZAUFpnRU0jLjYM5Tanh0YauUBXhAnL6GSSVJnScYYtkiNbqZCSXwkJSAYxITOuuZAfmchHR8kEZAZAtX4ywh5Tj5MqBgkDOVpSHUZD'

g=facebook.GraphAPI(ACCESS_TOKEN)

friends = g.get_object('me/friends')

surveytakers = [']

list_of_id = ['Natasha Sharma','Deeksha Tandon']
likes = []
for friend in friends['data']:
	for person in surveytakers:
		if friend['name'] == person:
			list_of_id.append(friend['id'])
			likes.append ({ friend['name'] : g.get_connections(friend['id'], "likes",limit=150)['data'] })


with open('likes.json','w') as outfile:
	json.dump(likes, outfile, indent=4)
"""
json_encoded = json.dumps(likes, indent=4)

print json_encoded
#["Latisha Khattar"][0]["id"]
"""
