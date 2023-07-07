
from dotenv import load_dotenv
load_dotenv()
import os
import requests

api_endpoint = 'https://nubela.co/proxycurl/api/linkedin/school/students/'
api_key = os.getenv("PROXYCURL_API_KEY")
header_dic = {'Authorization': 'Bearer ' + api_key}
params = {
    'linkedin_school_url': 'https://www.linkedin.com/school/stanford-university',
    'country': 'us',
    'enrich_profiles': 'enrich',
    'search_keyword': 'computer*|cs',
    'page_size': '100',
    'student_status': 'current',
    'sort_by': 'recently-matriculated',
    'resolve_numeric_id': 'false',
}
response = requests.get(api_endpoint,
                        params=params,
                        headers=header_dic)


from print_response import handle_response
handle_response(response)

# Not tested yet