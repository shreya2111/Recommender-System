import networkx as nx # pip install networkx
import requests # pip install requests
from networkx.readwrite import json_graph
from collections import Counter

import facebook
import json

import d3py

ACCESS_TOKEN='CAACEdEose0cBAHjZAlffZBWLYe25UbZCcJ1nZBZBd5qmMn1UviyH69qTZAi1t2ugvWZBeXpj2E58cdorJLIIcF5ijVgiLHCtEeKJq0ntz8HAWwTsS8fZA4w4HNsrdLXgcSEEjzxq6wZB5M7dBYpjCzNUYYd3b3xGDoR8t0XYRp7jwm6409sq3BwqQTdxR29xbQdz93LVkc9LvqZCZA05CcdAX9FSpHA45rFZAy4ZD'

url = 'https://graph.facebook.com/me/friends/%s?access_token=%s'

g=facebook.GraphAPI(ACCESS_TOKEN)

friends = g.get_connections("me", "friends")['data']

likes = { friend['name'] : g.get_connections(friend['id'], "likes")['data'] 
          for friend in friends }

mutual_friends={}


friends_likes_categories = Counter([like['category'] 
                                    for friend in likes 
                                      for like in likes[friend]])


nxg = nx.Graph()

[ nxg.add_edge('me', mf) for mf in friends_likes_categories]

[ nxg.add_edge(f1, f2) 
  for f1 in friends_likes_categories
      for f2 in friends_likes_categories[f1] ]

# Explore what's possible to do with the graph by 
# typing nxg.<tab> or executing a new cell with 
# the following value in it to see some pydoc on nxg
print nxg

nld=json_graph.node_link_data(nxg)
json.dump(nld,open('/home/shreya/Documents/category.json','w'))

with d3py.NetworkXFigure(nxg, width=500, height=500) as p:
    p += d3py.ForceLayout()
    p.show()
