import json
import os
import datetime

for i in range(9):
	try:
		os.chdir('../call_record/')
		
		with open('callsSortedperson_'+str(i)+'.json','r') as f:
			data=json.load(f)
		print 'User: ',i
		#print len(data)
		friends=[]
		
		for j in range(len(data)):
			#print data[j][0]
			friends.append(data[j][0])
						
	
			
		friends=list(set(friends))
		#print len(friends)
		#24 hour loop
				
		time=data[0][2]
		t=datetime.datetime.fromtimestamp(data[0][2]).strftime("%Y-%m-%d %H:%M:%S") #IST
		#print t
		
		calls=[]
		
		for k in friends:
			c=0
			for j in range(len(data)):
				if data[j][1]==2:
						
					#In 86400 seconds all outgoing calls to one person
					
					if k==data[j][0]:
						#if data[j][2]<=(float(time)+86400):
						t=datetime.datetime.fromtimestamp(data[j][2]).strftime("%Y-%m-%d %H:%M:%S") #IST
						#print t

						c+=1
						#print c,k
					

			calls.append(c)
		#print len(calls)
		k=[]
		c=0
		for j in range(len(friends)):
			k.append(j+1)
			if calls[j]==0:
				c+=1
		print c


		#print zip(k, calls)
	
		f=open('#CallsVsContacts'+str(i)+'.json','w')
		json.dump(zip(k,calls),f,indent=2)
						


	except Exception as e:
		continue



