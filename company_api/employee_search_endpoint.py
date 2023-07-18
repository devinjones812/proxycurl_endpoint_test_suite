import os
import requests
from print_response import handle_response
from dotenv import load_dotenv
load_dotenv()

# Just a heads-up before you run this: I think this costs a TON of credits...
# "Cost: 6/employee returned + 10 initial
# country: 3/employee returned

api_endpoint = 'https://nubela.co/proxycurl/api/linkedin/company/employee/search/'
api_key = os.getenv("PROXYCURL_API_KEY")
header_dic = {'Authorization': 'Bearer ' + api_key}
params = {
    'linkedin_company_profile_url': 'https://www.linkedin.com/company/microsoft/',
    'keyword_regex': 'ceo|cto',
    'page_size': '1',
    'country': 'us',
    'enrich_profiles': 'enrich',
    'resolve_numeric_id': 'false',
}
response = requests.get(api_endpoint,
                        params=params,
                        headers=header_dic)



handle_response(response)

# Super confusing... returns "You have run out of credits" every time it's run