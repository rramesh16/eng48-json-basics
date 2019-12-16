
import requests
import json

def nhs_location_getter():
    user_input1 = input('Please enter the first postcode')
    user_input2 = input('Please enter the second postcode')
    user_input3 = input('Please enter the third postcode')
    dictionary_post_codes = {'postcodes':[user_input1, user_input2, user_input3]
}
    json_body = json.dumps(dictionary_post_codes)

    base_url = 'http://api.postcodes.io/'
    path = 'postcodes/'

    headers = {'Content-Type':'application/json'}

    postcodes_post_response = requests.post(base_url+path, data=json_body, headers=headers)

    results = postcodes_post_response.json()['result']
    counter = 1
    for request in results:
        print(counter, '- Postcode:', request['result']['postcode'], 'with nhs_location at:', request['result']['nhs_ha'])
        counter += 1

