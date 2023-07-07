import os
import requests
from print_response import handle_response
from dotenv import load_dotenv
load_dotenv()


api_endpoint = 'https://nubela.co/proxycurl/api/disposable-email'
api_key = os.getenv("PROXYCURL_API_KEY")
header_dic = {'Authorization': 'Bearer ' + api_key}
params = {
    'email': 'steven@nubela.co',
}
response = requests.get(api_endpoint,
                        params=params,
                        headers=header_dic)



handle_response(response)

