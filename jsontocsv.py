import json
import pandas as pd
from settings import CSVFILE

def json_to_csv(JSONFILE):
    pass 
    # Load JSON data from the file
    with open(f'{JSONFILE}', 'r') as file:
        data = json.load(file)

    # Extract hits from the JSON structure
    # hits = data.get('secondary').get('hits').get('hits') # if any key ('secondary', 'hits', or 'hits') is missing, the get method will return None, and the next get call will raise a TypeError
    # hits = data['secondary']['hits']['hits'] # If any of the keys ('secondary', 'hits', or 'hits') do not exist, it raises a KeyError
    hits = data.get('secondary', {}).get('hits', {}).get('hits', []) # safe as it will not raise a KeyError or TypeError. If any key is missing, you get a default empty dictionary or list, so hits will always be a list, even if the keys don’t exist.

    # get the required fields
    required_fields = []
    for hit in hits:
        required_fields.append(
            {
                'id': hit.get('_id', {}),
                'is_private': hit.get('_source', {}).get('is_private',{}),
                'ref_number': hit.get('_source', {}).get('ref_number',{}),
                'subject': hit.get('_source', {}).get('subject',{}),
                'scopes_joined': hit.get('_source', {}).get('scopes_joined',{}),
                'expiration_date': hit.get('_source', {}).get('expiration_date',{}),
                'cert_type': hit.get('_source', {}).get('type',{}).get('level_1_display_name', {}),
                'issue_date': hit.get('_source', {}).get('issue_date',{}),
                'trademark': hit.get('_source', {}).get('trademark',{}),
                'id2': hit.get('_source', {}).get('id',{}),
                'org_name': hit.get('_source', {}).get('org_name',{}),
                'last_update_date': hit.get('_source', {}).get('last_update_date',{}),
                'country_code': hit.get('_source', {}).get('org',{}).get('address', {}).get('country', {}).get('iso2_code', {}),
                'country': hit.get('_source', {}).get('org',{}).get('address', {}).get('country', {}).get('name', {}),
                'org_name': hit.get('_source', {}).get('org',{}).get('name', {}),
                'org_id': hit.get('_source', {}).get('org',{}).get('id', {}),
                'org_type': hit.get('_source', {}).get('org',{}).get('type', {}),
                'manufacturer_name': hit.get('_source', {}).get('manufacturer_name',{}),
                'release_date': hit.get('_source', {}).get('release_date',{}),
                'phrase_suggest': hit.get('_source', {}).get('phrase_suggest',{}),
                'scope_categories': ', '.join(hit.get('scope_categories', {})),
                'status': hit.get('_source', {}).get('status',{}).get('level_1_display_name', {})
            }
        )

    # Convert list of dicts to a DataFrame
    df = pd.DataFrame(required_fields)

    # Save DataFrame to CSV
    df.to_csv(f'{CSVFILE}', index=False)
    print(f'Log--->Data has been written to {CSVFILE}\n')