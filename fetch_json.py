import facebook
import json

ACCESS_TOKEN='CAACEdEose0cBAEbvp0O8OnxdodZBbR16knR2AK02vfFMcMYZB8H8ZCQmUim7lxGn8L3jL4ce8UkajNCykvb8B9iA0Omg6ZA1JAP29IjGH0hqFofb9WMiu80ByQ2HdOKdnpKDQn6phKVZBrNq9QryeUBZBYXoxKmwLpVCIabJZCAu1mpeYt3yykMLNhHzORO8GAgxwnnCTZCD7mTVY9EpEZC2Qc5m9j0jNSCEZD'

g=facebook.GraphAPI(ACCESS_TOKEN)

friends = g.get_connections("me", "friends")['data']

#print friends['name'], 'with id',friends['id']

survey_takers=['Nilaksh Das','Akshat Bhattacharjee','Aditi Chawla','Latisha Khattar','Rahul Yadav Manuwas','Pallavi Monica Ekka','Nishant Pai','Adrita Chakraborty','Divya Baskaran','Adhiraj Rawat','Madhulika Mukherjee']

list_of_friends=[]
likes=[]

if friends['name'] in survey_takers:
	list_of_id.append(friend['id'])
	likes.append ({ friend['name'] : g.get_connections(friend['id'], "likes")['data'] })
	#print likes


with open('likes.json','rw+') as outfile:
	data=json.dump(likes, outfile, indent=4)


print data[

