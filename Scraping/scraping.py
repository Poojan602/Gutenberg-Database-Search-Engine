import re
import datetime

Book = []
author = []
tlist = []

for year in range(1996,2021):
	with open('GUTINDEX.'+str(year)+'.txt', 'r') as f:
	    flag = 0
	    lists = []
	    finallist = []
	    string2 = ''

	    t = {}
	    t['file_name'] = 'GUTINDEX.'+str(year)+'.txt'
	    t['file_process_startTime'] = str(datetime.datetime.now().time())#.strftime("%H:%M:%S")
	   
	    for index,line in enumerate(f):
	    	string1 = []	
	
	    	string1.append(re.split(r'\s{2,}', line))
	    	
	    	if(flag == 0):
	    		for strng in string1[0]:
	    			if(strng == 'TITLE and AUTHOR'):
	    				flag = 1
	    				break
	    	elif(flag == 1):
	    		if(len(line)!=1 or len(line)!=0):
	    			string2 += line
	    		if(len(line)==1 or len(line)==0):
	    			if(len(string2)!=0 and len(string2)!=1):
	    				if "[Language" not in string2:
	    					string2 = re.sub(r'\[[^(*)]*\]', "", string2)
	    					string2 = re.sub('\s+',' ',string2)
	    					finallist.append(string2)
	    				string2 = ''
	
	for flst in finallist:
		numbers_removed = ''.join([i for i in flst if not i.isdigit()])
		space_removed = re.sub('\s+',' ',numbers_removed)
		splitted = space_removed.split(', by')
	
		if(len(splitted)==2):
			Book.append(splitted[0].strip())
			author.append(splitted[1].strip())
		if(len(splitted)==1):
			Book.append(splitted[0].strip())
			author.append("Unknown") 

	t['file_process_endTime'] = str(datetime.datetime.now().time())#.strftime("%H:%M:%S")

	tlist.append(t)

dlist = []
for i in range(len(Book)):
	d = {}
	d['Book'] = Book[i]
	d['Author'] = author[i]
	dlist.append(d)

import pymongo

client = pymongo.MongoClient("mongodb://Poojan:Poojan@100.24.21.95/Cloud_Assignment")

db = client.Cloud_Assignment

collection = db.Author_Book
collection2 = db.time

collection.insert_many(dlist)
collection2.insert_many(tlist)



