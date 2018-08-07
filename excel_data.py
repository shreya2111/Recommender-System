import csv
import re
import json

survey_data=[]

with open('PS.csv','r') as csvfile:
        reader=csv.reader(csvfile)
        for row in reader:
		row[2]=row[2].split('-')
		survey_data.append(row[1])
            	survey_data.append(row[2])
    
with open('Survey_data.json','w') as data:
	 json.dump(survey_data, data, indent=4)
print survey_data
