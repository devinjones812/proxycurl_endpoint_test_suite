
from dotenv import load_dotenv
load_dotenv()
import os
import requests

api_endpoint = 'https://nubela.co/proxycurl/api/linkedin/profile/resolve'
api_key = os.getenv("PROXYCURL_API_KEY")
header_dic = {'Authorization': 'Bearer ' + api_key}
params = {
    'company_domain': 'gatesfoundation.org',
    'first_name': 'Bill',
    'similarity_checks': 'include',
    'enrich_profile': 'enrich',
    'location': 'Seattle',
    'title': 'Co-chair',
    'last_name': 'Gates',
}
response = requests.get(api_endpoint,
                        params=params,
                        headers=header_dic)


from print_response import handle_response
handle_response(response)

# Not tested yet