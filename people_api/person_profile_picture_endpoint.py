
from dotenv import load_dotenv
load_dotenv()
import os
import requests

api_endpoint = 'https://nubela.co/proxycurl/api/linkedin/person/profile-picture'
api_key = os.getenv("PROXYCURL_API_KEY")
header_dic = {'Authorization': 'Bearer ' + api_key}
params = {
    'linkedin_person_profile_url': 'https://www.linkedin.com/in/williamhgates/',
}
response = requests.get(api_endpoint,
                        params=params,
                        headers=header_dic)


from print_response import handle_response
handle_response(response)

# Not tested yet