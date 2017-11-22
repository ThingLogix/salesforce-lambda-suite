import requests


def lambda_handler(event, context):
    """
    This function updates a Salesforce record
    :param event: takes the following form:
        {
            'access_token' (required): your access token for OAuth in Salesforce
            'uri' (required) your uri for your salesforce org
            'sobject_id' (required) the sfid of your object
            'sobject_name' (required) the name of the sfid object
            'attributes': {
                ... list of attributes
                e.g "BillingCity": "San Francisco"
            }
        }
    :param context: lambda context
    :return: success or failure
    """

    url = event['uri'] + '/services/data/v40.0/sobjects/' + event['sfobject_name'] + '/' + event['sfobject_id']

    headers = {
        'Authorization': 'Bearer ' + event['access_token']
    }

    response = requests.post(url, event['attributes'], headers=headers)
    if 'error' in response:
        return {
            'error': response['error_description']
        }
    return response

