import os
import requests
from print_response import handle_response
from dotenv import load_dotenv
load_dotenv()


api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin/company/job/count'
api_key = os.getenv("PROXYCURL_API_KEY")
header_dic = {'Authorization': 'Bearer ' + api_key}
params = {
    'job_type': 'anything',
    'experience_level': 'anything',
    'when': 'past-month',
    'flexibility': 'anything',
    'geo_id': '92000000',
    'keyword': 'software',
    'search_id': '1586',
}
response = requests.get(api_endpoint,
                        params=params,
                        headers=header_dic)



handle_response(response)
