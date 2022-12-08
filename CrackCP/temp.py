import requests

sheety=requests.get('https://api.sheety.co/===================/crackTeBe/sheet1')

handle = [i['codeForcesHandle'] for i in sheety.json()['sheet1']]
print(handle)


