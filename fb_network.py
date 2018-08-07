import requests
import facebook
import json
from prettytable import PrettyTable
from collections import Counter

def pp(o):
	print json.dumps(o,indent=1)


base_url='https://graph.facebook.com/me'

fields='friends.fields(name),friends.fields(likes)'

ACCESS_TOKEN='CAACEdEose0cBAHjZAlffZBWLYe25UbZCcJ1nZBZBd5qmMn1UviyH69qTZAi1t2ugvWZBeXpj2E58cdorJLIIcF5ijVgiLHCtEeKJq0ntz8HAWwTsS8fZA4w4HNsrdLXgcSEEjzxq6wZB5M7dBYpjCzNUYYd3b3xGDoR8t0XYRp7jwm6409sq3BwqQTdxR29xbQdz93LVkc9LvqZCZA05CcdAX9FSpHA45rFZAy4ZD'


url='%s?fields=%s&access_token=%s' % \
    (base_url, fields, ACCESS_TOKEN,)


##print url

# Interpret the response as JSON and convert back
# to Python data structures
content = requests.get(url).json()

# Pretty-print the JSON and display it
json.dumps(content, open('/home/shreya/Documents/fb_network.json','w'))


g=facebook.GraphAPI(ACCESS_TOKEN)


#print 'Me'
#print '---------------'
##pp(g.get_object('me'))

#print 'My friends---------'

#pp(g.get_connections('me','friends'))
friends = g.get_connections("me", "friends")['data']

likes = { friend['name'] : g.get_connections(friend['id'], "likes")['data'] 
          for friend in friends }

print likes


#-----------------------------------------------------------------------

friends_likes = Counter([like['name']
                         for friend in likes 
                           for like in likes[friend]
                               if like.get('name')])

pt = PrettyTable(field_names=['Name', 'Freq'])
pt.align['Name'], pt.align['Freq'] = 'l', 'r'
[ pt.add_row(fl) for fl in friends_likes.most_common(10) ]

print 'Top 10 likes amongst friends'
print pt



