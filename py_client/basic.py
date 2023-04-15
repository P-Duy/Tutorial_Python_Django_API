import requests

# endpoint = "http://httpbin.org/status/200/"
endpoint = "http://httpbin.org/anything"

get_reponse = requests.get(endpoint, json ={"query":"Hello All"}) # HTTP Request
print(get_reponse.text) # print raw text response


# HTTP Request -> HTML
# REST API HTTP Request -> JSON
# JavaScript Object Nototion ~Python Dict

print(get_reponse.json()) # print JSON response
print(get_reponse.status_code) # print status code
