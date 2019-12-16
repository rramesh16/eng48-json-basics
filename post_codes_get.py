import requests
# Get request
# Do not have a body (JSON)
# They have a base url, path and arguements

# build url
base_url = 'http://api.postcodes.io/'
path = 'postcodes/'
arguments = 'e146gt'

# Making the request
request_response = requests.get(base_url+path+arguments)
print(request_response)

# Turning a request to dictionary ---> use .json()

dictionary_response = request_response.json()
print(dictionary_response)
print(dictionary_response['result']['admin_ward'])