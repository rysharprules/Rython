import datetime
import requests
import hashlib

def retrieve_keys():
    with open("keys.properties", 'r') as f:
        keys = f.read().splitlines()

    valid_keys = True
    public_key = keys[0].split('=')[1]
    private_key = keys[1].split('=')[1]

    if len(public_key) == 0 or len(private_key) == 0:
        valid_keys = False
        print('Update the keys.propeties file with your public and private keys to access the Marvel API. Please do so, and restart the program.')

    return valid_keys, public_key, private_key

valid, public_key, private_key = retrieve_keys()

if valid:
    character = input('Type the name of a Marvel character... ')
    ts = str(datetime.datetime.now().timestamp())
    hash = hashlib.md5((ts + private_key + public_key).encode())
    url = 'https://gateway.marvel.com:443/v1/public/characters?name=' + character + '&apikey=' + public_key + '&ts=' + ts + '&hash=' + hash.hexdigest()
    
    print('Searching for description for ' + character + '...')

    response = requests.get(url)
    data = response.json()['data']

    if len(data['results']) == 0:
        print('No information on ' + character + ' found. Are you sure you typed their name correctly?')
    else:
        print('Description: ' + data['results'][0]['description'])
