import requests

response = requests.get('https://api.ipify.org')
print(response.text)

# Path: DEVOPS/2.py