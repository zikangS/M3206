# M3206
* PROJECT NAME *


**Table of Content**
	
1. Introduction
1. Features
1. Installation 
1. Usage

**Introduction**
	
As a new worker in a new company, our manager wants us to create a programme with some specifications.The purpose of this programme is to read a log file in apache format and change it to json format.From the json file, This programme will analyse the results and make a statistic from that. The statistic is made from the point of view of securité and the commercial view.

**Features**

This program contains two main code :
		
* code 1 which convert the log file from apache format to json format
* code 2 which analyse the results make a statistic and display on a graphic interface

**Installation**

to use this program, you have to install python3 first. You can refer how to install python version 3 at https://www.python.org/downloads/  

**Usage**

How to execute the program :
*Reminder : Make sure you have install python version 3*
1. **Convert file in apache format to json format**
    1. Place yourself in the files where you install the program
            
            ~$ cd  [directory_name]/
    1. Execute the code converter.py of the programme using python 3 

            ~$ cd Téléchargements/python3 converter.py
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
			1- 
			2-
			3-
			4-
			5-
			6-
			7-
	
