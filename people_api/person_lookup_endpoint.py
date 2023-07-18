import os
import requests
from print_response import handle_response
from dotenv import load_dotenv
load_dotenv()


api_endpoint = 'https://nubela.co/proxycurl/api/linkedin/profile/resolve'
api_key = os.getenv("PROXYCURL_API_KEY")
header_dic = {'Authorization': 'Bearer ' + api_key}
params = {
    'company_domain': 'griptape.ai',
    'first_name': 'Kyle',
    'similarity_checks': 'include',
    'enrich_profile': 'skip',
    'location': 'Mercer Island',
    'title': 'CEO',
    'last_name': 'Roche',
}
response = requests.get(api_endpoint,
                        params=params,
                        headers=header_dic)



handle_response(response)
