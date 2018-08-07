from urllib2 import *
import socket
import urllib
import json


user_agent='Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/29.0'
#headers={'User-Agent': user_agent,
#    	'Content-type': 'application/json',
#	'Accept': 'application/json'} 

url="http://api-v2.applymagicsauce.com/auth"
customer_id=292
api_key="p1temdbgvgs6667clkscaivjob"

# this creates a password manager
passman =HTTPPasswordMgrWithDefaultRealm()

passman.add_password(None, url, customer_id, api_key)

authhandler=HTTPBasicAuthHandler(passman)
opener =build_opener(authhandler)
opener.addheaders=[('User-Agent',user_agent),
		('Content-type','application/json'),
		('Accept','application/json')]
opener.open(url)
install_opener(opener)

#req=Request(url,headers)
'''
try:
	response=urlopen(url, timeout=5)

except HTTPError as e:
	print 'error code: ',e.code

except URLError as e:
	print 'reason: ',e.reason

except socket.timeout as e:
	print type(e)

'''
