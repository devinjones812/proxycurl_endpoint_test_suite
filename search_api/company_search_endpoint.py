import os
import requests
from print_response import handle_response
from dotenv import load_dotenv
load_dotenv()

# Just a heads-up before you run this: I think this costs a TON of credits...
# "Cost: 35 credits / successful request base charge. + 3 credits / result returned.
# (Extra charges might be incurred if premium optional parameters are used)"


api_endpoint = 'https://nubela.co/proxycurl/api/search/company'
api_key = os.getenv("PROXYCURL_API_KEY")
header_dic = {'Authorization': 'Bearer ' + api_key}
params = {
    'public_identifier_not_in_list': 'stripe,amazon',
    'public_identifier_in_list': 'stripe,amazon',
    'enrich_profiles': 'enrich',
    'page_size': '100',
    'funding_raised_before': '2019-12-30',
    'funding_raised_after': '2019-12-30',
    'funding_amount_min': '1000000',
    'funding_amount_max': '1000000',
    'founded_before_year': '1999',
    'founded_after_year': '1999',
    'description': '(?i)medical device',
    'employee_count_min': '1000',
    'employee_count_max': '1000',
    'industry': '(?i)^(higher )?education$',
    'name': 'Technology',
    'follower_count_max': '1000',
    'follower_count_min': '1000',
    'type': 'NON_PROFIT',
    'city': 'Seattle|Los Angeles',
    'region': 'United States',
    'country': 'us',
}
response = requests.get(api_endpoint,
                        params=params,
                        headers=header_dic)



handle_response(response)
