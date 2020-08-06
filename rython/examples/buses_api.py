import requests

head_office = "NW51TL"
app_id = "2fae1003"
app_key = "eb1c28baf4bb0faf42636058bbeaa58e"


def call_postcode(postcode):
    resp = requests.post("http://api.postcodes.io/postcodes",
                         json={"postcodes": [postcode]},
                         params={
                             'app_id': app_id,
                             'app_key': app_key
                         }
                         ).json()
    return resp['result'][0]['result']['latitude'], resp['result'][0]['result']['longitude']


def get_place(postcode):
    latitude, longitude = call_postcode(postcode)
    r = requests.get("http://transportapi.com/v3/uk/places.json",
                     params={
                         'app_id': app_id,
                         'app_key': app_key,
                         'lat': latitude,
                         'lon': longitude,
                         'type': 'bus_stop'}).json()
    return r['member'][0]['atcocode'], r['member'][1]['atcocode']


def get_live_data(atcocode):
    r = requests.get(
        'http://transportapi.com/v3/uk/bus/stop/{}/live.json'.format(atcocode),
        params={
            'app_id': app_id,
            'app_key': app_key,
            'group': 'no',
            'nextbuses': 'yes'
        },
    ).json()

    i = 1
    if r['departures']:
        for departure in r['departures']['all']:
            print('Bus #' + str(i))
            dest = departure['direction']
            arr = departure['best_departure_estimate']
            line = departure['line_name']
            print(dest + ' - ' + arr + ' - ' + line)
            i = i + 1
    else:
        print("No bus stops found for " + atcocode + '\n')

atco1, atco2 = get_place(head_office)
get_live_data(atco1)
get_live_data(atco2)