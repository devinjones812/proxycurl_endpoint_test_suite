
from dotenv import load_dotenv
load_dotenv()
import os
import requests

api_endpoint = 'https://nubela.co/proxycurl/api/find/company/role/'
api_key = os.getenv("PROXYCURL_API_KEY")
header_dic = {'Authorization': 'Bearer ' + api_key}
params = {
    'role': 'ceo',
    'company_name': 'nubela',
    'enrich_profile': 'enrich',
}
response = requests.get(api_endpoint,
                        params=params,
                        headers=header_dic)


from print_response import handle_response
handle_response(response)

# Not tested yet