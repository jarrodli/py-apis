# sydney trains api 
# jarrod li

import requests, json

auth = ("NaYYW1MYeXojvrGROPLoXpTfXyoE8rU4zfrc")

response = requests.get("https://api.transport.nsw.gov.au/tp/v1/trip/", headers=('apikey NaYYW1MYeXojvrGROPLoXpTfXyoE8rU4zfrc'))

print(response.status_code)
