import requests
import json
import urllib3
from datetime import date
today = str(date.today())
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# set up connection parameters in a dictionary
gateway = { "ip" : input("Enter your Unifi dashboard address (either IP or the address WITHOUT the <https> and port number): "), "port" : input("Enter the port number <default is 8443>: ")}

# set REST API headers
headers = {"Accept": "application/json",
           "Content-Type": "application/json"}
# set URL parameters
loginUrl = 'api/login'
url = f"https://{gateway['ip']}:{gateway['port']}/{loginUrl}"
# set username and password
username = input("Enter your Unifi username: ")
password = input("Enter your Unifi password: ")
body = {
    "username": username,
    "password": password
}

# Open a session for capturing cookies
session = requests.Session()

# login
response = session.post(url, headers=headers,
                        data=json.dumps(body), verify=False)

# parse response data into a Python object
api_data = response.json()
loggedIn = 0

if api_data['meta']['rc'] == 'error':
        input('Login error. Please restart the program and try again')
else:
        print("Login success")
        loggedIn = 1

# Set up to get site name
getSitesUrl = 'api/self/sites'
url = f"https://{gateway['ip']}:{gateway['port']}/{getSitesUrl}"
response = session.get(url, headers=headers,
                       verify=False)
api_data = response.json()

# Parse out the resulting list of
responseList = api_data['data']
# pprint(responseList)
d = 'desc'
n = 'name'
nameList = []
descList = []
for items in responseList:
        descList.append(items.get('desc'))
        nameList.append(items.get('name'))

saveList = []
for i in range(len(nameList)):
        saveList.append("******************************")
        saveList.append(descList[i])
        saveList.append(" ")
        print(descList[i])
        getDevicesUrl = f"api/s/{nameList[i]}/stat/device"
        url = f"https://{gateway['ip']}:{gateway['port']}/{getDevicesUrl}"
        response = session.get(url, headers=headers,
                               verify=False)
        api_data = response.json()
        responseList = api_data['data']
        for device in responseList:
            print(f"MAC:            {device['mac']}")
            saveList.append(device['mac'])
            if device['state'] == 1:
                print('State:          online')
                saveList.append('online')
                saveList.append(' ')
            else:
                print('State:          offline')
                saveList.append('offline')
                saveList.append(' ')

with open(gateway['ip']+today+'.txt', 'w') as f:
        for line in saveList:
                f.write(line)
                f.write('\n')

f.close()
if loggedIn == 1:
        input("Text file created with all sites and device MAC addresses. Press ENTER to exit. ")
