import json
import datetime
import os

for i in range(5,13):
	print i
	x=os.chdir('../'+str(i)+'_probedata')
	try:

		with open("(u'edu.mit.media.funf.probe.builtin.CallLogProbe',).json",'r') as file:
			data=json.load(file)
	
			timestamp=[]
			for i in range(0,len(data)):
		
				#timestamp.append(datetime.datetime.fromtimestamp(data[i][2]).strftime("%Y-%m-%d %H:%M:%S")) #IST
				#timestamp.append(time.strftime('%d/%m/%Y %H:%M:%S',  time.gmtime(data[i][2]))) #GMT

				timestamp.append(data[i][2])

			timestamp=sorted(timestamp)

			#print timestamp

			with open("sorted_time.json",'w') as f:
				json.dump(timestamp,f,indent=2)


	except Exception as e:
		continue
	


