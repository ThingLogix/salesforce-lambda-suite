from lambdas.services import ForceApi
from lambdas.exceptions import InvalidArgument


def lambda_handler(event, context):
    """
    refreshes an access token with a refresh token with Salesforce
    :param event: {
      'refresh_token': your refresh token
      'client_id': your app client id
      'client_secret': your app client secret
    }
    :param context: lambda context
    :return: new access token
    """
    if 'refresh_token' not in event:
        raise InvalidArgument('You need a refresh_token in this function.')
    if 'client_id' not in event:
        raise InvalidArgument('You need a client_id in this function.')
    if 'client_secret' not in event:
        raise InvalidArgument('You need a client_secret in this function.')

    api = ForceApi(event['client_id'], event['client_secret'])
    response = api.refresh_access_token(event['refresh_token'])
    if 'error' in response:
        return {
            'error': response['error_description']
        }
    else:
        return response


