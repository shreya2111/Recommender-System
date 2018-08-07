import json
import os
import glob


for j in range(1,9):
	try:
		os.chdir("../"+str(j)+"_probedata")
		with open("(u'edu.mit.media.funf.probe.builtin.SmsProbe',).json",'r') as file:
			data=json.load(file)


		timestamp=[]
		for i in range(len(data)):
			timestamp.append(data[i][2])
		#print timestamp

		timestamp=sorted(timestamp)

		with open("sms.json",'w') as file:
			json.dump(timestamp,file,indent=2)

		time=[]
		if len(timestamp)>1:

			for i in range(len(timestamp)-1):
				time.append(abs(timestamp[i+1]-timestamp[i]))
				#print 'okay'
		else:
			continue		
	
		sum_time=0
		for i in range(len(time)):
			sum_time+=time[i]

			
		avg_time=sum_time/len(time)
		#print avg_time
		diff=0
		for i in range(len(time)):
			diff+=(time[i]-avg_time)**2
		#print diff
		var_time=diff/len(time) 
		#print var_time
		id1=zip(['Average of inter sms time',avg_time,'Variance of inter sms time',var_time])
	
		with open('Text_InterEvent.json','w') as outfile:
			json.dump(id1,outfile,indent=2)


	except Exception as e:
		continue
		
	

