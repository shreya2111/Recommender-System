import json
import os
import glob
import datetime


for i in range(5,6):
	try:
		os.chdir("../"+str(i)+"_probedata")
		with open("(u'edu.mit.media.funf.probe.builtin.SmsProbe',).json",'r') as file:
			sms=json.load(file)


		with open("(u'edu.mit.media.funf.probe.builtin.CallLogProbe',).json",'r') as file:
			call=json.load(file)

		data=call+sms
		timestamp=[]
		for j in range(0,len(data)):
			timestamp.append(data[j][2])

		timestamp=sorted(timestamp)
		time=[]

		if len(timestamp)>1:

			for i in range(len(timestamp)-1):
		
				time.append(abs(timestamp[i+1]-timestamp[i]))
		else:
			break

		
		sum_time=0
		for i in range(len(time)):
			sum_time+=time[i]

		avg_time=sum_time/len(time)

		diff=0
		for i in range(len(time)):
			diff+=(time[i]-avg_time)**2
		#print float(diff)
		var_time=diff/len(time) 
		#print int(var_time)
		id1=zip(['Average of inter call time',avg_time,'Variance of inter call time',var_time])
	
		with open('CallText.json','w') as outfile:
			json.dump(id1,outfile,indent=2)

	except Exception as e:
		continue

	

		

		
