import requests

query = 'https://ergast.com/api/f1/2021.json'

response = requests.get(query)
print(response.status_code)

res_dict = response.json()
print(res_dict)
#print(res_dict["weather"][0]["main"])