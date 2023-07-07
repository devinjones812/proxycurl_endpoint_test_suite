
from dotenv import load_dotenv
load_dotenv()
import os

# Just a heads-up before you run this: I think this costs a TON of credits...
# "Cost: 35 credits / successful request base charge. + 3 credits / result returned.
# (Extra charges might be incurred if premium optional parameters are used)"

import requests

api_endpoint = 'https://nubela.co/proxycurl/api/search/person/'
api_key = os.getenv("PROXYCURL_API_KEY")
header_dic = {'Authorization': 'Bearer ' + api_key}
params = {
    'country': 'US',
    'public_identifier_not_in_list': 'williamhgates,johnrmarty',
    'public_identifier_in_list': 'williamhgates,johnrmarty',
    'enrich_profiles': 'enrich',
    'page_size': '100',
    'current_company_funding_raised_before': '2019-12-30',
    'current_company_funding_raised_after': '2019-12-30',
    'current_company_funding_amount_min': '1000000',
    'current_company_funding_amount_max': '1000000',
    'current_company_founded_before_year': '1999',
    'current_company_founded_after_year': '1999',
    'current_company_description': '(?i)medical device',
    'current_company_employee_count_min': '1000',
    'current_company_employee_count_max': '1000',
    'current_company_industry': '(?i)^(higher )?education$',
    'current_company_follower_count_max': '1000',
    'current_company_follower_count_min': '1000',
    'current_company_type': 'NON_PROFIT',
    'current_company_city': 'Seattle|Los Angeles',
    'current_company_region': 'United States',
    'current_company_country': 'us',
    'skills': '(?i)accounting',
    'interests': '(?i)technology',
    'industries': '(?i)automotive',
    'summary': '(?i)founder',
    'headline': '(?i)founder',
    'city': 'Seattle|Los Angeles',
    'region': 'United States',
    'languages': 'Mandarin|Chinese',
    'linkedin_groups': '(?i)haskell',
    'past_company_name': 'Stripe|Apple',
    'current_company_name': 'Stripe|Apple',
    'past_job_description': '(?i)education',
    'current_job_description': '(?i)education',
    'past_company_linkedin_profile_url': 'https://www.linkedin.com/company/apple',
    'current_company_linkedin_profile_url': 'https://www.linkedin.com/company/apple',
    'current_role_before': '2019-12-30',
    'current_role_after': '2019-12-30',
    'past_role_title': '(?i)founder',
    'current_role_title': '(?i)founder',
    'education_school_linkedin_profile_url': 'https://www.linkedin.com/school/national-university-of-singapore/',
    'education_school_name': 'Caltech|Massachusetts Institute of Technology',
    'education_degree_name': '\bMBA\b',
    'education_field_of_study': '(?i)computer science',
    'last_name': 'Jackson|Johnson',
    'first_name': 'Sarah?',
}
response = requests.get(api_endpoint,
                        params=params,
                        headers=header_dic)


from print_response import handle_response
handle_response(response)

# Not tested yet