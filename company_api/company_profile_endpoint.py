import os
import requests
from print_response import handle_response
from dotenv import load_dotenv
load_dotenv()


api_endpoint = 'https://nubela.co/proxycurl/api/linkedin/company'
api_key = os.getenv("PROXYCURL_API_KEY")
header_dic = {'Authorization': 'Bearer ' + api_key}
params = {
    'url': 'https://www.linkedin.com/company/google/',
    'resolve_numeric_id': 'true',
    'categories': 'include',
    'funding_data': 'include',
    'extra': 'include',
    'exit_data': 'include',
    'acquisitions': 'include',
    'use_cache': 'if-present',
}
response = requests.get(api_endpoint,
                        params=params,
                        headers=header_dic)



handle_response(response)
