import requests

sheety=requests.get('https://api.sheety.co/aeffad5a770fb5eb8147b688c81c7747/crackTeBe/sheet1')

handle = [i['codeForcesHandle'] for i in sheety.json()['sheet1']]
print(handle)


