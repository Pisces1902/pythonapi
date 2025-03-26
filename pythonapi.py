import requests
import json
requests.packages.urllib3.disable_warnings()
from tabulate import tabulate

base_url = "https://sandboxdnac.cisco.com/"
def get_token():
    url = base_url + 'dna/system/api/v1/auth/token'
    header = {
        "Authorization" : "Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE=",
        "Content-Type" : "application/json"
    }

    response = requests.post(url, headers=header, verify=False)
    print(response.json())
    data = response.json()['Token']
    return data
get_token() 

def get_network():
    url = base_url + 'dna/intent/api/v1/network-device'
    header = {
       'X-auth-token': get_token()
    }
    response = requests.get(url, headers=header, verify=False)
    data = response.json()
    print(json.dumps(data, indent=4))
get_network()    