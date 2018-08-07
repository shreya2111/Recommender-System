import facebook
import json
from prettytable import PrettyTable
from collections import Counter

ACCESS_TOKEN='CAACEdEose0cBAMcdKrtAZCwKTQly9tSkfJtX8pTl85zF6lUIGaGQiHz1NoS3ETLecjWXkUW6tBlgZCN9nonn2V4lKBhzALNvrDT3ZBJRs09mouzHvhxdKHdRnwy7lNA2uJiLKeMZBLKqbpdG29VtKmT59z9QdQXXHvJReJSwetI8wt6X6JCtzV7lZBMXzbZBmaDyHTha54QOulH0fBV6Cq377obLkz1ZBAZD'

g=facebook.GraphAPI(ACCESS_TOKEN)

friends = g.get_connections("me", "friends")['data']

likes = { friend['name'] : g.get_connections(friend['id'], "likes")['data'] 
          for friend in friends }

print likes

"""
friends_likes_categories = Counter([like['category'] 
                                    for friend in likes 
                                      for like in likes[friend]])

pt = PrettyTable(field_names=['Category', 'Freq'])
pt.align['Category'], pt.align['Freq'] = 'l', 'r'
[ pt.add_row(flc) for flc in friends_likes_categories.most_common(10) ]

print "Top 10 like categories for friends"
print pt
"""
