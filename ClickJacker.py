#!/usr/bin/python
import urllib2
#Coded and Developed By Tibin Sunny
print("""\
 _______________________________________________________________
	   _____ _ _      _        _            _             
	 / ____| (_)    | |      | |          | |            
	| |    | |_  ___| | __   | | __ _  ___| | _____ _ __ 
	| |    | | |/ __| |/ /   | |/ _` |/ __| |/ / _ \ '__|
	| |____| | | (__|   < |__| | (_| | (__|   <  __/ |   
	 \_____|_|_|\___|_|\_\____/ \__,_|\___|_|\_\___|_|  
                                                     (Version 1.0)  
        #Developed By TibinSunny #Contact:tibinsunny95@gmail.com
		            Feel Free to Report Bugs
 ________________________________________________________________  
   """)
hdr = {'User-Agent':'Mozilla/5.0'}
opt=input("Enter 1:For Bulk url checking \nEnter 2:For Single url checking: ")
a=" "
if opt==1:
	file=raw_input("Enter the path to text file (c:/asd/example.txt):  ")
	fh = open(file)
        for line in fh:
        	#print(line)
		if "http" not in line:
                	tester_tibin="https://"+line
                
                try:
                	req = urllib2.Request(tester_tibin,headers=hdr)
                	response = urllib2.urlopen(req)
                	code=response.getcode()
                	headers = response.info()
                	"""if code == 301:
                                tester_tibin=response.geturl()
                                a="Got Redirected to["+tester_tibin+"] site which"
	       		        req = urllib2.Request(tester_tibin,headers=hdr)
                                response = urllib2.urlopen(req)
                                headers = response.info()"""
	        	#print response.info()
	        	if  "X-Frame-Options: DENY" or "X-Frame-Options: SAMEORIGIN" in headers:
				out_url=tester_tibin+a+"is Not Vulnerable"
				print out_url
				print " "
	        	#elif "X-Frame-Options: SAMEORIGIN":
		        	#out_url=tester_tibin+ " Is Vulnerable with Same Origin(manual test required)"
				#print out_url
				#print " "
	        	else:
		        	out_url=tester_tibin+a+" Is Vulnerable"
				print out_url
				print " "
		except:
  			print(tester_tibin +"   Cannot be reached")
    			print " "
elif opt==2:
	url = raw_input("Enter the Domain name  :")
	tester_tibin=url
	if "http" not in url:
		tester_tibin="http://"+url
    	req = urllib2.Request(tester_tibin,headers=hdr)
        response = urllib2.urlopen(req)
	headers = response.info()
	redirect=response.geturl()
	code=response.getcode()
	"""if code == 301:
                tester_tibin=response.geturl()
                req = urllib2.Request(tester_tibin,headers=hdr)
                response = urllib2.urlopen(req)
                headers = response.info()
                a=1"""
	if  "X-Frame-Options: DENY" or "X-Frame-Options: SAMEORIGIN" in headers:
		out_url=tester_tibin+a+"is Not Vulnerable"
		print out_url
	#elif "X-Frame-Options: SAMEORIGIN":
        	#out_url=tester_tibin+ " Is Vulnerable with Same Origin(manual test required)"
		#print out_url
		#print " "
	
	else:
		out_url=tester_tibin+a+" Is Vulnerable"
		print out_url
		print " "

