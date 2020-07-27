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

def call_marvel(func):
  def decorator(*args, **kwargs):
    print('Searching for a description for ' + character + '...')
    return func(*args, **kwargs).json()['data']
  return decorator

@call_marvel
def call_name_search(url, private_key, public_key, character):
    return requests.get(append_keys(url + '?name=' + character.replace(' ', '%20'), private_key, public_key))


@call_marvel
def call_by_id(url, private_key, public_key, id):
    return requests.get(append_keys(url + '/' + str(id) + '?', private_key, public_key))


@call_marvel
def call_name_starts_with_search(url, private_key, public_key, character):
    return requests.get(append_keys(url + '?nameStartsWith=' + character.replace(' ', '%20'), private_key, public_key))

def append_keys(url, private_key, public_key):
    ts = str(datetime.datetime.now().timestamp())
    hash = hashlib.md5((ts + private_key + public_key).encode())
    return url + '&apikey=' + public_key + '&ts=' + ts + '&hash=' + hash.hexdigest()

def are_results_empty(data):
    if len(data['results']) == 0:
        return True
    return False

def print_description(data):
    print('Description: ' + data['results'][0]['description'])

searching, public_key, private_key = retrieve_keys()
url = 'https://gateway.marvel.com:443/v1/public/characters'

while searching:
    character = input('Type the name of a Marvel character... ')

    data = call_name_search(url, private_key, public_key, character)
    
    if are_results_empty(data):
        print('No information on ' + character + ' found. Trying "starts with" search...')
        data = call_name_starts_with_search(url, private_key, public_key, character)
        if are_results_empty(data):
            print('No information on ' + character + ' found. Are you sure you typed their name correctly?')
        else:
            if len(data['results']) == 1:
                print('Result found for character: ' + data['results'][0]['name'] + '\n')
                print_description(data)
                break
            else:
                print('Multiple results found. Please select one of the following characters to get a description...')
                i = 0
                for result in data['results']:
                    print(str(i) + ': ' + data['results'][i]['name'])
                    i += 1
                character_id = input('Enter the id for the character you\'d like to get a description for. If the character is not in the list, please enter \'N\' to re-enter the character name...')
                if character_id == 'N':
                    continue
                # Lazy solution, recall call_name_search with the name. More robust solution is to use id obtained
                # character = data['results'][int(character_id)]['name']
                # print_description(call_name_search(url, private_key, public_key, character))
                id = data['results'][int(character_id)]['id']
                print_description(call_by_id(url, private_key, public_key, id))
                break
    else:
        print_description(data)
        break
