import os
import requests
from print_response import handle_response
from dotenv import load_dotenv
load_dotenv()


api_endpoint = 'https://nubela.co/proxycurl/api/linkedin/profile/email'
api_key = os.getenv("PROXYCURL_API_KEY")
header_dic = {'Authorization': 'Bearer ' + api_key}
params = {
    'linkedin_profile_url': 'https://www.linkedin.com/in/jonjones1/',
    'callback_url': 'https://webhook.site/29e12f17-d5a2-400a-9d08-42ee9d83600a',
}
response = requests.get(api_endpoint,
                        params=params,
                        headers=header_dic)



handle_response(response)

# Returns a webhook