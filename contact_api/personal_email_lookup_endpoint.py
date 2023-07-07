import os
import requests
from print_response import handle_response
from dotenv import load_dotenv
load_dotenv()


api_endpoint = 'https://nubela.co/proxycurl/api/contact-api/personal-email'
api_key = os.getenv("PROXYCURL_API_KEY")
header_dic = {'Authorization': 'Bearer ' + api_key}
params = {
#    'twitter_profile_url': 'https://www.twitter.com/proxycurl',
#    'facebook_profile_url': 'https://www.facebook.com/zuck',
    'linkedin_profile_url': 'https://linkedin.com/in/kyleroche',
    'email_validation': 'include',
    'page_size': '0',
}
response = requests.get(api_endpoint,
                        params=params,
                        headers=header_dic)


handle_response(response)

# You can include only one of the following URLs at a time: Twitter, Facebook, LinkedIn
