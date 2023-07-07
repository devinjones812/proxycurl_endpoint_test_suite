import os
import requests
from print_response import handle_response
from dotenv import load_dotenv
load_dotenv()


api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin/company/job'
api_key = os.getenv("PROXYCURL_API_KEY")
header_dic = {'Authorization': 'Bearer ' + api_key}
params = {
    'job_type': 'anything',
    'experience_level': 'entry_level',
    'when': 'past-month',
    'flexibility': 'remote',
    'geo_id': '92000000',
    'keyword': 'software engineer',
    'search_id': '1035',
}
response = requests.get(api_endpoint,
                        params=params,
                        headers=header_dic)



handle_response(response)

# This endpoint is also found under the "search_api/job_search_endpoint" path