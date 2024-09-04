import requests
import json
from settings import JSONFILE
from jsontocsv import json_to_csv
# API endpoint
url = 'https://ocs-iecee-api.iecee.org/api/search-es'

# Headers
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'en-US,en-KE;q=0.9,en-GB;q=0.8,en;q=0.7',
    'Content-Type': 'application/json',
    'Cookie': 'ocs_iecee_api_prd_session=8v4fkQA7vGGJl8KxymKMmOiKm5GxlOZOTdusRnZ1; _ga_WZGGKSTGM1=GS1.1.1725420241.1.1.1725421155.0.0.0; AWSALB=T5DMLDNvFQDL+S+it+1YoEwLJL4762uYgTcN+pm/8bZkNe2B1oZwHDZRNtaSrIVP3LcDjlYEFR3uXDbC7etG4hRyQzk6kZqIYKgPpP/6TfyhpnEcy6bvlKllLO2w; AWSALBCORS=T5DMLDNvFQDL+S+it+1YoEwLJL4762uYgTcN+pm/8bZkNe2B1oZwHDZRNtaSrIVP3LcDjlYEFR3uXDbC7etG4hRyQzk6kZqIYKgPpP/6TfyhpnEcy6bvlKllLO2w',
    'DNT': '1',
    'Origin': 'https://certificates.iecee.org',
    'Referer': 'https://certificates.iecee.org/',
    'Sec-CH-UA': "'Chromium';v='128', 'Not;A=Brand';v='24', 'Google Chrome';v='128'",
    'Sec-CH-UA-Mobile': '?0',
    'Sec-CH-UA-Platform': 'macOS',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
}

# Payload
payload = {
    'from': 1,
    'size': 15,
    'query': '',
    'sortBy': [{'ref_number': 'asc'}],
    'dateRanges': {},
    'conjunctiveFacetGroups': [],
    'terms': {},
    'mode': 'PARTIAL'
}

# POST request
response = requests.post(url, json=payload, headers=headers)

# Status code and process the response
if response.status_code == 200:
    data = response.json()
    # Write JSON data to a file
    with open(f'{JSONFILE}', 'w') as file:
        json.dump(data, file, indent=4)
    print(f'\nLog--->Data has been written to {JSONFILE}')
else:
    print(f'Log--->Failed to retrieve data: {response.status_code}')


# convert json to csv
json_to_csv(JSONFILE)