# !/urs/bin/python3

import json
import re


#fonction pour ouvrir et lire le fichier json (return une liste de dictionnaires)
def open_file():
	with open(filename) as json_data:
		d = json.load(json_data)
	return d

#fonction pour analyser des plages horaires de réception des demandes
def time_range():
	midnight=0
	morning=0
	afternoon=0
	night=0
	for i in open_file() :
		if re.findall('\:([0][0-5])\:\d\d\:',i['time']) :
			midnight=midnight+1
		elif re.findall('\:(0[6-9]|1[0-1])\:\d\d\:',i['time']) :
			morning=morning+1
		elif re.findall('\:(1[2-7])\:\d\d\:',i['time']) :
			afternoon=afternoon+1
		elif re.findall('\:(1[8-9]|2[0-3])\:\d\d\:',i['time']) :
			night=night+1
	
	total=midnight+morning+night+afternoon
	print('<< User time analysis >>')
	print('Midnight  (00h-05h) : ['+'■'*round(midnight/total*40)+']  ' + "{:.2f}".format(midnight/total*100) +'%')
	print('Morning   (06h-11h) : ['+'■'*round(morning/total*40)+']  ' + "{:.2f}".format(morning/total*100) +'%')
	print('Afternoon (12h-17h) : ['+'■'*round(afternoon/total*40)+']  ' + "{:.2f}".format(afternoon/total*100) +'%')
	print('Night     (18h-23h) : ['+'■'*round(night/total*40)+']  ' + "{:.2f}".format(night/total*100) +'%')
	
	
#fonction pour analyser des différentes erreurs 	
def analyse_response():
	error_404=0
	error_304=0
	error_301=0
	error_206=0
	error_403=0
	error_500=0
	error_416=0
	ok=0
	for i in open_file() :
		if re.findall('[4][0][4]',i['response']) :
			error_404+=1
		elif re.findall('[3][0][1]',i['response']) :
			error_301+=1
		elif re.findall('[3][0][4]',i['response']) :
			error_304+=1
		elif re.findall('[2][0][0]',i['response']) :
			ok+=1
		elif re.findall('[2][0][6]',i['response']) :
			error_206+=1
		elif re.findall('[4][0][3]',i['response']) :
			error_403+=1
		elif re.findall('[5][0][0]',i['response']) :
			error_500+=1
		elif re.findall('[4][1][6]',i['response']) :
			error_416+=1
		
	
	total=ok +error_404+error_304+error_301+error_206+error_403+error_500+error_416
	
	print('<< Error analysis >>')
	print('OK            : ['+'■'*round(ok/total*40)+']  ' + "{:.2f}".format(ok/total*100) +'%')
	print('Error 206     : ['+'■'*round(error_206/total*40)+']  ' + "{:.2f}".format(error_206/total*100) +'%')
	print('Error 301     : ['+'■'*round(error_301/total*40)+']  ' + "{:.2f}".format(error_301/total*100) +'%')
	print('Error 304     : ['+'■'*round(error_304/total*40)+']  ' + "{:.2f}".format(error_304/total*100) +'%')
	print('Error 404     : ['+'■'*round(error_404/total*40)+']  ' + "{:.2f}".format(error_404/total*100) +'%')
	print('Error 403     : ['+'■'*round(error_403/total*40)+']  ' + "{:.2f}".format(error_403/total*100) +'%')
	print('Error 416     : ['+'■'*round(error_416/total*40)+']  ' + "{:.2f}".format(error_416/total*100) +'%')
	print('Error 500     : ['+'■'*round(error_500/total*40)+']  ' + "{:.2f}".format(error_500/total*100) +'%')
	
	


#fonction pour analyser des page web demandé (plus de 100)
def analyse_page():
	page={}
	page['initial']=0
	total=0
	for i in open_file() :
		x=0
		for k in list(page) : #forcer des changements dans la dictionnaire
			if i['referrer'] == k :
				page[k]=int(page[k])+1
				x+=1
		if x==0 :
			page[i['referrer']]=1	
	#visit de webpage totale
	for x in page :
		total+=page[x]
	
	print('<<Page visit analysis>>')
	
	#visit de webpage plus de 100
	for l in page :
		if page[l] > 100 :
			if l != '-' :
				print('Webpage : '+l)
				print('['+'■'*round(page[l]/total*100)+']  ' +"{:.2f}".format(page[l]/total*100) +'%')
			
#fonction pour analyser des IP adresses qui envoient des demandes (plus de 100)			
def analyse_ip():
	count={}
	count['initial']=0
	total=0
	for i in open_file() :
		x=0
		for k in list(count) : #force change in disctionary
			if i['remote_ip'] == k :
				count[k]=int(count[k])+1
				x+=1
		if x==0 :
			count[i['remote_ip']]=1	
	#ip total 
	for x in count :
		total+=count[x]
	
	print('<<IP address analysis>>')
	
	#visit de ip plus de 100
	for l in count :
		if count[l] > 100 :
			print('IP address : '+l)
			print('['+'■'*round(count[l]/total*100)+']  ' +"{:.2f}".format(count[l]/total*100) +'%')
	


#fonction pour analyser des tailles de paquets
def bytes_finder() :
    byte_table_grand=[]
    byte_table_moyenne=[]
    byte_table_petit=[]
    ctr=0  #counter to count '-'
    for i in open_file() :
        if i['bytes']!='-':
            if int(i['bytes'])<10000:
                byte_table_petit.append(i['bytes'])
            if int(i['bytes'])>10000 and int(i['bytes'])<50000 :
                byte_table_moyenne.append(i['bytes'])
            if int(i['bytes'])>50000:
                byte_table_grand.append(i['bytes'])    
        else:
            ctr=ctr+1
    total=len(byte_table_grand)+len(byte_table_moyenne)+len(byte_table_petit)+ctr
    
    
    print('<<Bytes analysis>>')
    print('Big packet      (more than 50001 bytes)  : ['+'■'*round(len(byte_table_grand)/total*40)+']  ' + "{:.2f}".format(len(byte_table_grand)/total*100) +'%')
    print('Average packet  (10001-50000 bytes)      : ['+'■'*round(len(byte_table_moyenne)/total*40)+']  ' + "{:.2f}".format(len(byte_table_moyenne)/total*100) +'%')
    print('Big packet      (1-10000 bytes)          : ['+'■'*round(len(byte_table_petit)/total*40)+']  ' + "{:.2f}".format(len(byte_table_petit)/total*100) +'%')
	





#fonction pour analyser des machines utilisés lesquelles les demandes ont été envoyé
def analyse_machine():
	Linux=0
	Windows=0
	iPhone=0
	Macintosh=0
	Android=0
	nothing=0
	HTC=0
	for i in open_file() :
		if re.findall('X11',i['os']) :
			Linux+=1
		elif re.findall('Windows',i['os']) :
			Windows+=1
		elif re.findall('iPhone',i['os']) :
			iPhone+=1
		elif re.findall('Macintosh',i['os']) :
			Macintosh+=1
		elif re.findall('Android',i['os']) :
			Android+=1
		elif re.findall('-',i['os']) :
			nothing+=1
		elif re.findall('HTC',i['os']) :
			HTC+=1
			
	
	total=Linux+Windows+iPhone+Macintosh+Android+nothing+HTC
	
	print('<< Machine analysis >>')
	print('Linux               : '+'['+'■'*round(Linux/total*40)+']  ' + "{:.2f}".format(Linux/total*100) +'%')
	print('Windows             : '+'['+'■'*round(Windows/total*40)+']  ' + "{:.2f}".format(Windows/total*100) +'%')
	print('Macintosh           : '+'['+'■'*round(Macintosh/total*40)+']  ' + "{:.2f}".format(Macintosh/total*100) +'%')
	print('iPhone              : '+'['+'■'*round(iPhone/total*40)+']  ' + "{:.2f}".format(iPhone/total*100) +'%')
	print('Android             : '+'['+'■'*round(Android/total*40)+']  ' + "{:.2f}".format(Android/total*100) +'%')
	print('HTC                 : '+'['+'■'*round(HTC/total*40)+']  ' + "{:.2f}".format(HTC/total*100) +'%')
	print('Bots                : '+'['+'■'*round(nothing/total*40)+']  ' + "{:.2f}".format(nothing/total*100) +'%')

#fonction pour le choix d'analysis 
def option_stats (n) :
	if n==1:
		time_range()
	elif n==2:
		analyse_machine()
	elif n==3:
		analyse_response()
	elif n==4:
		analyse_page()
	elif n==5:
		analyse_ip()
	elif n==6:
		bytes_finder()
	elif n==7:
		print('')
		time_range()
		print('')
		print('__________________________________________________________________________________')
		print('')		
		analyse_machine()
		print('')
		print('__________________________________________________________________________________')
		print('')
		analyse_response()
		print('')
		print('__________________________________________________________________________________')
		print('')
		analyse_page()
		print('')
		print('__________________________________________________________________________________')
		print('')
		analyse_ip()
		print('')
		print('__________________________________________________________________________________')
		print('')
		bytes_finder()
		exit()
	elif n==8:
		exit()
	else :
		print('Input 1-8 only')


filename=str(input('File name? -->'))

print("Option:")
print(" 1: << User time analysis >>")
print(" 2: << Machine analysis >>")
print(" 3: << Error analysis >>")
print(" 4: <<Page visit analysis>>")
print(" 5: <<IP address analysis>>")
print(" 6: <<Bytes analysis>>")
print(" 7: All")

user_option= int(input('Option -->'))
option_stats (user_option)

while True :
	print('')
	print('__________________________________________________________________________________')
	print('')
	print('Voulez-vous faire une autre choix?')
	print("Option:")
	print(" 1: << User time analysis >>")
	print(" 2: << Machine analysis >>")
	print(" 3: << Error analysis >>")
	print(" 4: <<Page visit analysis>>")
	print(" 5: <<IP address analysis>>")
	print(" 6: <<Bytes analysis>>")
	print(" 7: All")
	print(" 8: No")
	
	user_option= int(input('Option -->'))
	option_stats (user_option)
	
	




