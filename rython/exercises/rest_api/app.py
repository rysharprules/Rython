import requests

# get json with information
print('GET http://rem-rest-api.herokuapp.com/api/users')
response = requests.get('http://rem-rest-api.herokuapp.com/api/users')
if response.status_code != 200:
    raise ApiError('GET /api/users {}'.format(response.status_code))

#print(resp) # <Response [200]>
#print(resp.json) # <bound method Response.json of <Response [200]>>

#for json in resp.json():
#   print(json) # data # offset # limit # total

data = response.json() # convert json to Python object 

for users in data['data']:
    print('{} {} {}'.format(users['id'], users['firstName'], users['lastName']))
    """
    1 Peter Mackenzie
    2 Cindy Zhang
    3 Ted Smith
    4 Susan Fernbrook
    5 Emily Kim
    6 Peter Zhang
    7 Cindy Smith
    8 Ted Fernbrook
    9 Susan Kim
    10 Emily Mackenzie
    """

print('\nPOST http://rem-rest-api.herokuapp.com/api/monster')
monster = {"name": "Godzilla", "location": "Tokyo"}
response = requests.post('http://rem-rest-api.herokuapp.com/api/monster', json=monster)
data = response.json()
print(data) # {'name': 'Godzilla', 'location': 'Tokyo', 'id': 1}

print('\nPUT http://rem-rest-api.herokuapp.com/api/monster/1')
response = requests.put('http://rem-rest-api.herokuapp.com/api/monster/1', json={"id": 1, "name": "Gojira", "location": "Tokyo"})
data = response.json()
print(data) # {'id': 1, 'name': 'Gojira', 'location': 'Tokyo'}

print('\nDELETE http://rem-rest-api.herokuapp.com/api/monster/1')
response = requests.delete('http://rem-rest-api.herokuapp.com/api/monster/1')
data = response.json()
print(data) # None