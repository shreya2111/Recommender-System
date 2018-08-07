import datetime as dt
import os
import json
import get_distance as gd
import re

#################################
#	Use this script for 	# 
#	Radius of Gyration	#
#	Distance travelled	#  
#	Number of places	#
#################################



for i in range(5,13):
	try:
		os.chdir("../"+str(i)+'_probedata')
		print "User: ",i
		# Reading location data(latitude, longitude,timestamp)
		with open("(u'edu.mit.media.funf.probe.builtin.LocationProbe',).json",'r') as f:
			data=json.load(f)

		loc=[]
		for j in data:
		
			#print dt.datetime.fromtimestamp(j[2]).strftime("%Y-%m-%d %H:%M:%S")
			try:
				found=re.search("mIsFromMockProvider\":false,(.+?)\"mProvider\":", j[1]).group(1)
				latitude=re.search("mLatitude\":(.+?),\"mLongitude\":",found).group(1)
				longitude=re.search("mLongitude\":(.+?),",found).group(1)
				#print latitude,longitude
				x=zip([j[2],latitude,longitude])
				loc.append(x)				
				
			
			except AttributeError:	
				continue

		z=[j for j in range(len(loc))]
			
		with open("location_data.json",'w') as f:
			json.dump(loc,f,indent=2)

		with open("LocationForEntropy.json",'w') as f:
			json.dump(zip(z,loc),f,indent=2)

			
		f=open('location_data.json','r')
		data=json.load(f)
		
		
		time=[]
		dis=[]
		max_d=0
		x=data[0][0][0]
		for j in range(len(data)-1):
			if data[j][0][0]<=(x+86400):

				#timestamp difference, lat1,long1 lat2,long2
				#ignoring single data point log
				di=gd.distance(float(data[j][1][0]),float(data[j][2][0]),float(data[j+1][1][0]),float(data[j+1][2][0]))
				#print 'di',di
				for k in range(j+1,len(data)):
					d=gd.distance(float(data[j][1][0]),float(data[j][2][0]),float(data[k][1][0]),float(data[k][2][0]))
					#print 'd: ',d
					if d>max_d:
						max_d=d	
						#print 'd>max',max_d	

				time.append(data[j+1][0][0]-data[j][0][0])
				dis.append(di)
		print "maximum_distance",max_d
			
		#print len(time),len(dis),time,dis
		j=zip(time,dis)
		
		f=open('Location.json','w')
		json.dump(zip(time,dis),f,indent=2)
		
		distance_travelled=sum(dis)
		rad=max_d/2
		n=0
		for j in dis:
			if j>50:
				n+=1

		#Entropy of places

		f=open('LocationForEntropy.json','r')
		data=json.load(f)
		id1=[]
		count=[]
		for j in range(len(data)-1):
			for k in range(j+1,len(data)):
			if gd.distance(float(data[j][1][1][0]),float(data[j][1][2][0]),float(data[k][1][1][0]),float(data[k][1][2][0]))<=50:
				id1.append(

		
		print 'radius_of_gyration in meters',rad
		print 'Distance travelled in a day',distance_travelled
		print 'Number of places', n	
		with open('SpatialData.json','w') as f:
			json.dump([['Radius of gyration',rad],['Distance travelled in a day',distance_travelled],['Number of places',n]],f,indent=2)
				
		 
	except Exception as e:
		continue
	
