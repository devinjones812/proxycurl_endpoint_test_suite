import os
import requests
from print_response import handle_response
from dotenv import load_dotenv
load_dotenv()


api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
api_key = os.getenv("PROXYCURL_API_KEY")
header_dic = {'Authorization': 'Bearer ' + api_key}
params = {
    'url': 'https://www.linkedin.com/in/kyleroche/',
    'fallback_to_cache': 'on-error',
    'use_cache': 'if-present',
    'skills': 'include',
    'inferred_salary': 'include',
    'personal_email': 'include',
    'personal_contact_number': 'include',
    'twitter_profile_id': 'include',
    'facebook_profile_id': 'include',
    'github_profile_id': 'include',
    'extra': 'include',
}
response = requests.get(api_endpoint,
                        params=params,
                        headers=header_dic)



handle_response(response)
