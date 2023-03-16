import requests
import json
import re

def aipdb():
    # Defining the api-endpoint
    url = 'https://api.abuseipdb.com/api/v2/check'
    x = input("Enter Your IP:\n")
    pattern = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    regex = re.compile(pattern)
    if regex.match(x):
        pass
    else:
        print("ENTER CORRECT IP")
        quit()
    querystring = {
        'ipAddress': x,
        'maxAgeInDays': '90'
    }

    headers = {
        'Accept': 'application/json',
        'Key': 'enter your api key here'
    }

    response = requests.request(method='GET', url=url, headers=headers, params=querystring)
    '''
    # Formatted output
    decodedResponse = json.loads(response.text)
    data=json.dumps(decodedResponse, sort_keys=True, indent=4)
    print(data["data"]["abuseConfidenceScore"])
    '''
    data=response.json()
    abuseConfidenceScore=data["data"]["abuseConfidenceScore"]
    ipAddress=data["data"]["ipAddress"]
    #countryName=data["data"]["countryName"]
    usageType=data["data"]["usageType"]
    isp=data["data"]["isp"]
    domain=data["data"]["domain"]
    totalReports=data["data"]["totalReports"]
    isPublic=data["data"]["isPublic"]
    countryCode=data["data"]["countryCode"]
    #=data["data"][""]

    def printdetails():
        print("IP ADDRESS: ",ipAddress,"\n",
        "isPublic: ",isPublic,"\n",
        "abuseConfidenceScore: ",abuseConfidenceScore,"\n",
        "totalReports: ",totalReports,"\n",
        "usageType: ",usageType,"\n",
        "countryCode: ",countryCode,"\n",
        "isp: ",isp,"\n",
        "domain: ",domain,"\n",)
        
        
        

    if abuseConfidenceScore==0:
        print('\x1b[32m'+'🟢 CLEAN \n'+'\x1b[0m')
        printdetails()
    else:
        print('\x1b[31m'+"🔴 MALICIOUS \n"+'\x1b[0m')
        printdetails()
        
    print(response.json())

while True:
    aipdb()
    answer = input("\n Do you want to search anything else? (y/n): ")
    if answer.lower() == "n":
        break