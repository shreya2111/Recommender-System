import json
import os
import glob
import re

for j in range(5,6):
	try:

		os.chdir('../'+str(j)+'_probedata')
		#print "FOLDER NAME:",j

		for file in glob.glob("(u'edu.mit.media.funf.probe.builtin.CallLogProbe',).json"):
			
			name=str(file)
		
			timestamp=[]
			with open(name,'r') as file:
				data=json.load(file)

			for i in range(len(data)):
				timestamp.append(data[i][2])
			#print "Timestamp:", timestamp
			time=[]
			timestamp = sorted(timestamp)
			if len(timestamp)>1:

				for i in range(len(timestamp)-1):
					#print i
					time.append(abs(timestamp[i+1]-timestamp[i]))
					#print "time: ",time[i]
			else:
				break

	
			with open('Timestamp.json','w') as outfile:
				json.dump(time,outfile,indent=2)
		
		
			sum_time=0
			for i in range(len(time)):
				sum_time+=time[i]

			avg_time=sum_time/len(time)
			#print avg_time
			diff=0
			for i in range(len(time)):
			
				#print "Timestamp["+str(i)+"]: ",time[i], " Average: ",avg_time, "Difference: ",time[i]-avg_time
				diff+=(time[i]-avg_time)**2
			#print "Difference Var: ",diff
			var_time=diff/len(time) 
			#print var_time
			id1=zip(['Average of inter call time',avg_time,'Variance of inter call time',var_time])
		
			with open('Call_InterEvent.json','w') as outfile:
				json.dump(id1,outfile,indent=2)
		
	except Exception as e:
		continue
	
			
				
	


	
