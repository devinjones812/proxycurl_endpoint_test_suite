import os
import requests
from print_response import handle_response
from dotenv import load_dotenv
load_dotenv()

# Just a heads-up before you run this: I think this costs a TON of credits...
# "Cost: 3/employee returned PLUS
# role_search: 6/employee returned + 10 initial
# country: 3/employee returned

api_endpoint = 'https://nubela.co/proxycurl/api/linkedin/company/employees/'
api_key = os.getenv("PROXYCURL_API_KEY")
header_dic = {'Authorization': 'Bearer ' + api_key}
params = {
    'url': 'https://www.linkedin.com/company/microsoft',
    'country': 'us',
    'enrich_profiles': 'enrich',
    'role_search': '(co)?-?founder',
    'page_size': '100',
    'employment_status': 'current',
    'sort_by': 'recently-joined',
    'resolve_numeric_id': 'false',
}
response = requests.get(api_endpoint,
                        params=params,
                        headers=header_dic)



handle_response(response)

# This took FOREVER to load and I think it might've literally sucked up like
# 800 credits in the process (went from ~824 -> 42). I didn't even let it run to completion.