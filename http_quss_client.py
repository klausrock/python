"""
HTTP-QuSS  Client 
©Copyright by ISS-IP Holding LLC - Delaware USA

Prototype
---------

Version : 1.0
Date    : 13/09/2023 
Author  : Dipl.-Ing.(FH) Klaus Rock
WEB Site: https://http-quss.com
E-Mail  : klaus.rock@iss-ip.com

 -------------------              ------------------           ------------------         
:                   :            :                  :         :                  :        
:  TCP WEB Browser  :            : HTTP-QuSS Client :         : HTTP-QuSS Server :        
:   Client 1 - N    :            : Client Listener  :         :   UDP Listener   :        
:                   :            :                  :         :                  :
:   IPv4 | IPv6     :            :   IPv4 | IPv6    :         :   IPv4 | IPv6    :                
:  TCP Port xxxxx   :<----:      :  UDP Port xxxxx  :<------->:  UDP Port 10000  :          ------------------
:                   :     :      :                  :         :                  :         :                  :  
 -------------------      :      : Bandwidth Mbit/s :         : Bandwidth Mbit/s :         :     HTTP-QuSS    :
                          :      :    MTU Bytes     :         :    MTU Bytes     :         :  Rendering Grid  :
 -------------------      :      :     RTT ms       :         :     RTT ms       :         :      Engine      :          ------------------
:                   :     :      :                  :         :                  :         :                  :         :                  :
:     TCP Tunnel    :     :      :   IPv4 | IPv6    :         :    IPv4 | IPv6   :         :    IPv4 | IPv6   :         :  Apache Forward  :
:    Client 1 - N   :     :----->:   TCP Port 80    :         :   TCP Port xxxxx : <------>:    TCP Port 80   :         :   Proxy Cache    :
:                   :     :      :                  :         :                  :         :                  :         :                  :    
:    IPv4 | IPv6    :     :       ------------------           ------------------          :    IPv4 | IPv6   :         :    IPv4 | IPv6   :
:   TCP Port xxxxx  :<----:                                                                :   TCP Port xxxx  :<------->:   TCP Port 8080  :       
:                   :                                                                      :                  :         :                  :
 -------------------                                                                        ------------------           ------------------
         :                                                                                      
         :
         V                                                                                                                                                                                                             
"""

import sys
import os
import mod_error_dictonary as error_numbers
import mod_client_json as client_data

if client_data.str_runtime_error != '0':
    error_numbers.print_error_message(client_data.str_runtime_error)
    sys.quit()

import mod_random_payload as random_payload

# Client License Data

print ()
print ('Client License Data:')
print ('--------------------')
print ()
print (client_data.strClient_Licensee)
print (client_data.strClient_City)
print (client_data.strClient_ZIP)
print (client_data.strClient_Street)
print (client_data.strClient_Country)
print (client_data.strClient_License_Number)
print (client_data.strClient_License_ID)
print (client_data.strClient_Valid)
print (client_data.strClient_Latitude)
print (client_data.strClient_Longitude)
print (client_data.strClient_TCP_Port)
print (client_data.strClient_Max_Clients)

# HTTP-QuSS Server 1 Data

print ()
print ('HTTP-QuSS Server 1 Data:')
print ('------------------------')
print ()
print (client_data.strServer_City)
print (client_data.strServer_Country)
print (client_data.strServer_Latitude)
print (client_data.strServer_Longitude)
print (client_data.strServer_IPv4)
print (client_data.strServer_IPv6)
print (client_data.strServer_UDP_Port)
print (client_data.strServer_Bandwidth)
print (client_data.strServer_MTU)
print (client_data.strServer_RTT)

# Generate Payload Random Byte String for Socket Testing

print("\nGenerate Payload Random Byte String for Socket Testing")
payload=random_payload.random_payload(1499)
print("\nLength = ", len(payload))
print("\n",payload)
