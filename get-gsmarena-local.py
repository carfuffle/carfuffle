#!/usr/bin/python

from bs4 import BeautifulSoup
#import re
import os, sys
import csv
#only needed in python2
import unicodecsv

#log = open('/home/carfuffle/get-gsmarena-local.log','a')
csvFile = open('/home/carfuffle/phone_data.csv','wb')
#csvFile = open('/home/carfuffle/phone_data.csv','wb',encoding='utf-8') # Only works in python3
csvWriter = unicodecsv.writer(csvFile)

links = []

# read file names into variable
walk_dir = os.path.abspath('/home/carfuffle/gsmarena')
#walk_dir = os.path.abspath('/home/carfuffle/gsmarena')
#print('walk_dir (absolute) = ' + os.path.abspath(walk_dir))
for root, subdirs, files in os.walk(walk_dir):
        for file in files:        
                #print os.path.join(root,file)
		links.append(os.path.join(root,file))	

#for link in links:
#	print(link)


header = []
data = []
phones = []
#soup = BeautifulSoup(open(link), "lxml")
soup = BeautifulSoup(open(links[0]), "lxml")
tables = soup.find_all('table')
#table = soup.find('table')
#print(tables)
header.append('phone')
for table in tables:
	td = table.find_all('td', 'ttl')
	#print(td)
	for ttl in td:
		#phones.append(link)
		#print(ttl.text)
		header.append(ttl.text)


csvWriter.writerow(header)

for link in links:
	print(link)
	#data(clear)
	data.append(link)
	soup = BeautifulSoup(open(link), "lxml")
	tables = soup.find_all('table')
	for table in tables:
		td = table.find_all('td', 'nfo')
		#print(td)
		for nfo in td:
			print(nfo.text)
			#data.append(link)
			data.append(nfo.text)

#debug
print(len(header))
print(len(data))
#for dat in data:
###	print(dat)
csvWriter.writerow(data)


#for spec in data:
#	print(spec)
	#csvWriter.writerow(spec)

#log.close()
csvFile.close()
