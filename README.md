# Introduction
This is a project to extract all the Test Certificates from [IECEE Website](https://certificates.iecee.org/#/search). IECEE (IEC System of Conformity Assessment Schemes for Electrotechnical Equipment and Components) is a body of the International Electrotechnical Commission (IEC) that adminsters the IEC CB Scheme. This scheme is a CB Scheme is multilateral agreement to allow international certification of electrical and electronic products so that a single certification allows worldwide market access

> $${\color{red} Disclaimer: This project is intended for educational and research purposes only. Unauthorized use of the IECEE data or API may violate their terms of service. Please ensure that your usage complies with the IECEE’s policies and guidelines. This API is functional as at the date of last commit. Changes to the structure of data or the IECEE portal may affect the functionality of this API. }$$

# Install Requirements
Obviously a virtual environment is recommended. 
Run `pip install -r requirements.txt` 

# IECEE Certificates Portal
The IECEE Certificates Portal is a web-based tool that allows users to search for and retrieve Test Certificates for various electrical and electronic products. These certificates are part of the CB Scheme, which streamlines the certification process across multiple countries.

# Functionalities
This project includes several functionalities designed to interact with the IECEE Certificates Portal, extract data, and process it for various use cases. The structure of the API is as follows:

## The API
The project uses a custom API to fetch Test Certificates data programmatically. The certificates data is publicly available. 

### API Endpoint
The endpoint for the API was generated by the Google Chrome website inspection window as <https://ocs-iecee-api.iecee.org/api/search-es>. 
This allows querying of Test Certificates data.
Endpoint declaration:
```python
# API endpoint
url = "https://ocs-iecee-api.iecee.org/api/search-es"

```

### Payload
```python 
payload = {
    "from": 1,
    "size": 9999, # this is the maximum number
    "query": "", # example: "philips"
    "sortBy": [{"ref_number": "asc"}],
    "dateRanges": {},
    "conjunctiveFacetGroups": [],
    "terms": {},
    "mode": "PARTIAL"
}
```

### Headers
While the headers may not be necessary for this API, they are included in the script. Some servers require some headers items like the User-Agent for security and monitoring purposes.

## JSON Data to Structured Data
Once the JSON data is retrieved from the API, it is converted into structured data formats such as CSV. This step involves parsing the JSON response and extracting relevant fields to be stored in a tabular format. Some of the unnecessary data is removed.

For this project, the following fields were retained:
- id
- is_private
- ref_number
- subject
- scopes_joined
- expiration_date
- cert_type
- issue_date
- trademark
- id2
- org_name
- last_update_date
- country_code
- country
- org_id
- org_type
- manufacturer_name
- release_date
- phrase_suggest
- scope_categories
- status

## Data to MySQL Database
After converting the JSON data into a structured format, the next step is to insert this data into a MySQL database. Check for a future update on this.

### Connection String
While this script does not have a connection to a DB like MySQL, the connection is pretty-straight forward. This may be updated in future for the data to be saved directly to a DB.

> Note: The portal has 1.5 million (*1,564,968 certificates* as at the time of the commit date), however, to prevent overloading the IECEE Server (and possibly being blocked), the payload in this project has been set to a size of 15, which is the default number of items (certificates) per page when opened on a browser. You can change `from` and `sisze` variables to get data from different parts/pages of the portal. Of course, you may use other means to bypass this (BUT, remember the IECEE policies mentioned above!)

```json
"hits": {
            "total": {
                "value": 1564968,
                "relation": "eq"
            },
        "........."
}
```

# JSON to CSV
While the data can be converted directly to csv instead of saving the file to a `.json` first, this step has been maintained for purposes of separating these two processes and ease of porting files to other storage means.
