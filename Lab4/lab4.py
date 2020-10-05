
import http.client
import urllib
import time
from random import randint
from time import sleep

key = "54CDA6FJF4RCJ92C"  # Put your API Key here
def thingSpeakUpload():
        #My values for email, group, and identifier
        cmail = "coltonnorth@cmail.carleton.ca"
        group = "L2-M-9"
        identifier = "B"
        sleep(1)

        #Send email
        params = urllib.parse.urlencode({'field1': cmail,'field2': group,'field3': identifier,'key':key }) 
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = http.client.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print("email address: {} \nProject Group: {} \nIdentifier: {}".format(cmail, group, identifier))
            print(response.status, response.reason)
            data = response.read()
            conn.close()
        except:
            print("connection failed")
        
if __name__ == "__main__":
                thingSpeakUpload()
