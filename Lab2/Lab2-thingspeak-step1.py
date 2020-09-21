
import http.client
import urllib
import time
from random import randint
from time import sleep

key = "VIWW4MGAGGG9ZW14"  # Put your API Key here
def thermometer():
    while True:
        #Gives random number between 0 and 50 to upload
        temp = randint(0,50) # Get Random number
        sleep(1)
        params = urllib.parse.urlencode({'field1': temp, 'key':key }) 
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = http.client.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print(temp)
            print(response.status, response.reason)
            data = response.read()
            conn.close()
        except:
            print("connection failed")
        break
if __name__ == "__main__":
        while True:
                thermometer()
