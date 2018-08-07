import networkx as nx # pip install networkx
import requests # pip install requests
from networkx.readwrite import json_graph
import facebook
import json
import d3py

#ACCESS_TOKEN='CAACEdEose0cBADJtRP13eLNEnfdEePtnIjbji2iYxcFzi1cKDwKfO75DjiBG1X47DpHh2BWzIOu3KzZCjA6RyU2cC9wIAYdR68RfEZAuC6xmCt8CrXZCr3Yl0v2N5dZBLe3kZAzmmPjKgIUiOPukoAk2YsxeooWl6SmNpWxEBUZCBdZB6STPV0NmhBVECC0ZA67YIZAdvx63QrBnGmB6Qd6YZAWPX632R9M6YZD'

ACCESS_TOKEN='CAACEdEose0cBAFqaiaSJ8X6XY3m437XseE8n5Pg7k6G6MLehRDrMJveNPTouPpXqBwlDp8nRh6FljZChXBoYIzSh6HX3slAV3IZAL0jRceD9UsQz9yebaXbw6YC3GRwqosPqTGR25uF92G9HvhTScZAmJzLEJiLPJLzuvOqZA82gI5ZBGFNZCg7O5Y0dbKFrNxmx9meLj6rla9j61bvHmFkyL5MzwXhiQZD'
g=facebook.GraphAPI(ACCESS_TOKEN)

friends = [ (friend['id'], friend['name'])
                for friend in g.get_connections('me', 'friends')['data'] ]

url = 'https://graph.facebook.com/me/mutualfriends/%s?access_token=%s'

mutual_friends = {} 

# This loop spawns a separate request for each iteration, so
# it may take a while. Optimization with a thread pool or similar
# technique would be possible.
for friend_id, friend_name in friends:
    r = requests.get(url % (friend_id, ACCESS_TOKEN,) )
    response_data = json.loads(r.content)['data']
    mutual_friends[friend_name] = [ data['name'] 
                                    for data in response_data ]
    
nxg = nx.Graph()

[ nxg.add_edge('me', mf) for mf in mutual_friends ]

[ nxg.add_edge(f1, f2) 
  for f1 in mutual_friends 
      for f2 in mutual_friends[f1] ]

# Explore what's possible to do with the graph by 
# typing nxg.<tab> or executing a new cell with 
# the following value in it to see some pydoc on nxg
print nxg

nld=json_graph.node_link_data(nxg)
json.dump(nld,open('/home/shreya/Documents/force.json','w'))

with d3py.NetworkXFigure(nxg, width=500, height=500) as p:
    p += d3py.ForceLayout()
    p.show()
