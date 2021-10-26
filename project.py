# !/urs/bin/python3

import re
import json

#fonction pour ouvrir et lire le fichier log (return une liste)
def open_file(_file) :
	with open(_file, 'r') as f:
		l = f.readlines()
	return l

#fonction pour trouver des plages horaires de réception des demandes
def find_time(_line):
    result=re.findall("\[([^\]]+)\]",_line) #qqch entre des crochets 
    return(result[0])
 
#fonction pour trouver des IP adresses 
def find_remote_ip(_line):
    result=re.findall("([\d]+\.[\d]+\.[\d]+\.[\d]+)", _line)
    return(result[0])#le premier qui respecte x.x.x.x

#fonction pour trouver des IP adresses  
def find_response(_line):
    result=re.findall("\"[^\"]+\"\s([\d|\-]+)", _line)
    return(result[0]) #des chiffres apres le guimet "..."

#fonction pour trouver des bytes    
def find_bytes(_line):
    result=re.findall("\"[^\"]+\"\s[\d]+\s([\d|\-]+)", _line) 
    return(result[0]) #des chiffres apres le guimet "..." suivi par des chiffres xxx 

#fonction pour trouver des tous les guimets     
def find_guimet(_line) :   
    return(re.findall('"([^\"]+|-?)"',str(_line))) #tous les guimets

#fonction pour trouver des systèmes d'exploitation	
def os_finder(_string_user_agent) :
	os_list=['X11','Windows','iPhone','Macintosh','Android']
	if any (x in _string_user_agent for x in os_list):
		Os=re.findall('\(([^\)]+)\)',str(_string_user_agent))
		if len(Os)==0 :
			Os=['-','-']
	else:
		Os=['-','-']
	return Os[0]

#fonction pour compter s'il y a trois guimets
def count_guimet(_line) :
	tru=1
	if len(find_guimet(_line))<3:
		tru=0
	return tru


#fonction pour creer une dictionnaire avec des cles
def create_dict(_line):
	dic={}
	dic['time']=find_time(_line)
	dic['remote_ip']=find_remote_ip(_line)
	dic['request']=find_guimet(_line)[0]
	dic['response']=find_response(_line)
	dic['bytes']=find_bytes(_line)
	dic['referrer']=find_guimet(_line)[1]
	dic['system_agent']=find_guimet(_line)[2]
	dic['os']=os_finder(find_guimet(_line)[2])	
	return(dic)


def read_lines(_file) :
	grand_liste=[]
	counter=0
	for line in open_file(_file) :
		counter=counter+1
		if count_guimet(line) == 0 : #si guimets mois que 3
			print ("line "+str(counter)+" has error!") #trouver des lignes avec des errors
		else:
			grand_liste.append(create_dict(line))
		
	return(grand_liste)

	


filename=str(input('File name? -->')) #le nom de fichier log
destination=str(input('Destination file name ? -->')) #le nom de fichier json qu'on veut stocker les infos

json_object = json.dumps(read_lines(filename), indent = 4)
  
#ecrire dans le fichier json
with open(destination, "w") as outfile:
    outfile.write(json_object)

