import json

def handle_response(response):
    # 200: successful request, 404: webpage not found, 202: webhooks
    if response.status_code == 200 or response.status_code == 404 or response.status_code == 202:
        try:
            response_dict = response.json()
            pretty_json_output = json.dumps(response_dict, indent=4)
            print(pretty_json_output)
        except json.JSONDecodeError:
            print("Failed to decode JSON from response")

    elif response.status_code == 429:
        print('Usage rate limited. Retrying may be necessary.')
    elif response.status_code == 400:
        print('Invalid parameters provided. Refer to the Proxycurl documentation and message body for more info.')
    elif response.status_code == 401:
        print('Invalid API Key')
    elif response.status_code == 403:
        print('You have run out of credits')
    elif response.status_code == 500:
        print('There is an error with the API. Please contact Proxycurl for assistance')
    elif response.status_code == 503:
        print('Enrichment failed, please retry')
    else:
        print('Unknown error occurred. HTTP Status Code: {}'.format(response.status_code))
