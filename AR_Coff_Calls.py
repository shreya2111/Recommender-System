from __future__ import print_function
import json
import datetime
import os
import csv
import pandas as pd
import numpy as np
import statsmodels.api as sm
from dateutil.parser import parse
import matplotlib.pyplot as plt
import pylab as p

#Probes with no sorted_time.json or call log
#2,4,8,9,10,11,12
#Good files: {1,3}(less data),5,6,7

for i in range(1,13):
	try:
		print('User: %d'%i)
		
		x=os.chdir('../'+str(i)+'_probedata')

		with open("sorted_time.json",'r') as file:
			timestamp=json.load(file)

	
		#1month,31 days,31*24/6 periods of 6 hrs			
		L= [[0 for x in range(2)] for x in range(124)] 
		T=timestamp[0]
	
		for k in range(124):

			T+=3600*6	
			c=0
			for j in range(1,len(timestamp)):
				if T>timestamp[j] and (T-3600*6)<timestamp[j]:
					c+=1	
			
			t=datetime.datetime.fromtimestamp(T).strftime("%Y-%m-%d %H:%M:%S") #IST		
			L[k][0]=t		
			L[k][1]=c #Contains the number of calls made in the 6-hr period
		#print(L)
			
		t=datetime.datetime.fromtimestamp(timestamp[-1]).strftime("%Y-%m-%d %H:%M:%S") #IST		
		for k in range(124):
			if L[k][0]>t:
				#print(L[k][0],t)
				L=L[:k]
				break
		#print('length %f' %len(L))	
					
		start=str(L[0][0])
		end=str(L[-1][0])
		dates=pd.date_range(parse(start,dayfirst=True), parse(end,dayfirst=True), freq='6h')
		time_series=pd.TimeSeries([int(nb[1]) for nb in L], index=dates)
	
		ar_model=sm.tsa.AR(time_series, freq='A')
		ar_res=ar_model.fit(maxlag=9, method='mle', disp=-1)
		#ar_result=sm.tsa.AR.ARResults(ar_,ar
		print('The parameters of the model for order 9 are below: ')
		params=(ar_res.params)
		print(params)
		
		
	
		#pred=sm.tsa.AR.predict(params,start=None, end=None)
		#print(pred)
	
		#Plotting data
		"""
		k=time_series.resample('M',how='mean').plot(label="# of calls per 6 hr for a month")
		plt.xlabel('time')
		plt.ylabel('# of calls')
		plt.legend()	
		plt.show()
		"""


	


		#Savings data in csv, json formats
	
		with open("time_series.csv",'wb') as f:
			writer=csv.writer(f, delimiter=',')
			for row in L:
				writer.writerows([row])

		data=open("time_series.json",'w') 
		json.dump(L,data,indent=2)

		data=open("ARCoff.json",'w') 
		json.dump(str(params),data,indent=2)
		
	except Exception as e:
		continue



