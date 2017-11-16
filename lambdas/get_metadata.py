from lambdas.exceptions import InvalidArgument
import requests


def lambda_handler(event, context):
    """
    This function gets all metadata for a given account in Salesforce
    :param event: takes the following form:
        {
            'access_token' (required): your access token for OAuth in Salesforce
            'client_id' (required) your client id,
            'client_secret' (required) your client secret
            'uri' (required) your uri for your salesforce org
        }
    :param context: lambda context
    :return: metadata in JSON form
    """

    if 'access_token' not in event:
        raise InvalidArgument('Invalid arguments. Make sure you are including "access_token" in your request.')
    if 'client_id' not in event:
        raise InvalidArgument('Invalid arguments. Make sure you are including "client_id" in your request.')
    if 'client_secret' not in event:
        raise InvalidArgument('Invalid arguments. Make sure you are including "client_secret" in your request.')

    url = event['uri'] + '/services/data/v40.0/sobjects/'

    headers = {
        'Authorization': 'Bearer ' + event['access_token']
    }
    response = requests.get(url, headers=headers).json()
    if 'error' in response:
        return {
            'error': response['error_description']
        }
    return response



