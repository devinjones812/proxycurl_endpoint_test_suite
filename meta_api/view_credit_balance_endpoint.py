
from dotenv import load_dotenv
load_dotenv()
import os
import requests

api_endpoint = 'https://nubela.co/proxycurl/api/credit-balance'
api_key = os.getenv("PROXYCURL_API_KEY")
header_dic = {'Authorization': 'Bearer ' + api_key}
response = requests.get(api_endpoint,
                        headers=header_dic)


from print_response import handle_response
handle_response(response)
