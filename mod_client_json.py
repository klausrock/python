"""
### mod_client_json.py

Read the Client License and HTTP-Quss Server Data from 
http_quss_client.json

### Prototype 

Version : 1.0
Date    : 13/09/2023 
Author  : Dipl.-Ing.(FH) Klaus Rock
WEB Site: https://http-quss.com
E-Mail  : klaus.rock@iss-ip.com

### Modules

json

### Variables

#### Run-Time Error Return Code

str_runtime_error

#### Client License Data

strClient_Licensee :
strClient_City :   
strClient_ZIP :
strClient_Street :
strClient_Country :
strClient_License_Number :
strClient_License_ID :
strClient_Valid :
strClient_Latitude :
strClient_Longitude :
strClient_TCP_Port :
strClient_Max_Clients

#### HTTP-QuSS Server Data

strServer_City :
strServer_Country :
strServer_Latitude :
strServer_Longitude :
strServer_IPv4 :
strServer_IPv6 :
strServer_UDP_Port :
strServer_Bandwidth :
strServer_MTU :
strServer_RTT :

### Functions
none
"""

# See Module mod_error_dictonary.py

str_runtime_error='0'
import json

try:
  
    # Opening http_quss_client.json

    json_file = open('http_quss_client.json')
 
    # returns JSON object as a dictionary

    data = json.load(json_file)

except FileNotFoundError:

    str_runtime_error='1000'

else:

    # Access a value via the key

    strlicense=data['Client License']
    strserver=data['HTTP-QuSS Server 1']

    # Read Client License Data

    strClient_Licensee=strlicense['Licensee']
    strClient_City=strlicense['City']
    strClient_ZIP=strlicense['ZIP']
    strClient_Street=strlicense['Street']
    strClient_Country=strlicense['Country']
    strClient_License_Number=strlicense['License Number SHA-256']
    strClient_License_ID=strlicense['License ID']
    strClient_Valid=strlicense['Valid']
    strClient_Latitude=strlicense['Latitude']
    strClient_Longitude=strlicense['Longitude']
    strClient_TCP_Port=strlicense['TCP Port']
    strClient_Max_Clients=strlicense['Max Clients']

    # Read HTTP-QuSS Server 1

    strServer_City=strserver['City']
    strServer_Country=strserver['Country']
    strServer_Latitude=strserver['Latitude']
    strServer_Longitude=strserver['Longitude']
    strServer_IPv4=strserver['IPv4']
    strServer_IPv6=strserver['IPv6']
    strServer_UDP_Port=strserver['UPD Port']
    strServer_Bandwidth=strserver['Bandwidth Mbit/s']
    strServer_MTU=strserver['MTU 1500']
    strServer_RTT=strserver['RTT x 100']
 
finally:

    # Closing http_quss_client.json file

    json_file.close()
