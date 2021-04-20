import requests
import socket
import sh
from tqdm import tqdm
import time

socket.gethostbyname(socket.gethostname())
print("----- Network Detail -----")
print("  ")
print("++++++++++++++++++++++++++++++")
print("//Author: madKrypton")
print("++++++++++++++++++++++++++++++")
print(" ")
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print(f"Hostname: {hostname}")
print(f"Host Address: {ip_address}")
print(" ")
print("External ip/public ip:")
print(requests.get('http://ip.42.pl/raw').text)
print(" ")
print(" Checking Current Devices in the Network")
print("- - - - - - - - - - - - - - - - - - - - -")
print(" ")
print("//Example:  10.10.1.")
ipadd=input("Enter the first 3 Octect of your Ip: ")
for num in tqdm (range(1,14),
 desc="Analysising…", 
               ascii=False, ncols=70):
    time.sleep(0.01) 
    ip = ipadd+str(num)  
  
    try:  
        sh.ping(ip, "-c 1",_out="/dev/null")  
        print ("  |   PING ",ip , "OK")  
        print("- - - - - - - - - - - - - - - - - - - - -")
    except sh.ErrorReturnCode_1:  
        print ("  |   PING ", ip, "FAILED" )
print("Execution  Finished..")
