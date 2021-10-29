# M3206
* Automatisation des tâches d’administration système *


**Table of Content**
	
1. Introduction
1. Features
1. Installation 
1. Usage
1. Project Members

**Introduction**
	
As a new worker in a new company, our manager wants us to create a programme with some specifications.The purpose of this programme is to read a log file in apache format and change it to json format.From the json file, This programme will analyse the results and make a statistic from that. The statistic is made from the point of view of securité and the commercial view.

**Features**

This program contains two main code :
		
* project.py which convert the log file from apache format to json format
* stat.py which analyse the results make a statistic and display on a graphic interface

**Installation**

To use this program, you have to install python3 first. You can refer how to install python version 3 at https://www.python.org/downloads/  

**Usage**

How to execute the program :

* Reminder : Make sure you have install python version 3*
* all lines in log file are in LogFormat : "%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-agent}i\""*

1. **Convert file in apache format to json format**
    1. Place yourself in the files where you install the program
            
            ~$ cd  [directory_name]/
    1. Execute the code project.py of the programme using python 3 

            ~$ cd Téléchargements/python3 project.py
    1. Insert the log file name (apache format) 

            ~$ python3 project.py
            File name? --> log.txt
    1. Insert the name you want the file to be saved as (with extension json : exemple.json )
        
            ~$ python3 project.py
            File name? --> log.txt
            Destination file name ? --> example.json
        **The json file will be saved in the same directory as the code* 
1. **Create a statistic from a json file**
    1. Execute the code stat.py of the programme using python 3 
			
			~$ python3 stat.py
            File name? --> example.json
	1. Select an option from (1-7) according to your choice
	
			Option:
			1 : User time analysis
			2 : Machine analysis
			3 : Error analysis
			4 : Page analysis
			5 : IP address analysis
			6 : Bytes analysis
			7 : All
**Project Members**
1. SIAU Zi Kang
1. BIN ABDUL SHUKOR Muhammad Ariff
