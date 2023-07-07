import os
import requests
from print_response import handle_response
from dotenv import load_dotenv
load_dotenv()

# Just a heads-up before you run this: I think this costs a TON of credits...
# Cost depends on which parameters you're using (used ~4,000 credits in 3 calls)

api_endpoint = 'https://nubela.co/proxycurl/api/linkedin/school/students/'
api_key = os.getenv("PROXYCURL_API_KEY")
header_dic = {'Authorization': 'Bearer ' + api_key}
params = {
    'linkedin_school_url': 'https://www.linkedin.com/school/stanford-university',
    'country': 'us',
    'enrich_profiles': 'skip',
    'search_keyword': 'null',
    'page_size': '10',
    'student_status': 'current',
    'sort_by': 'recently-matriculated',
    'resolve_numeric_id': 'false',
}
response = requests.get(api_endpoint,
                        params=params,
                        headers=header_dic)



handle_response(response)
