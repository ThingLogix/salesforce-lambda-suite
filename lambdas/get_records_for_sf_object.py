import requests


def lambda_handler(event, context):
    """
    This function updates a Salesforce record
    :param event: takes the following form:
        {
            'access_token' (required): your access token for OAuth in Salesforce
            'uri' (required) your uri for your salesforce org
            'sobject_name' (required) the name of the sfid object
            'fields' (optional) if you want filtered results with only certain fields, put them in this array
            []
        }
    :param context: lambda context
    :return: success or failure
    """

    headers = {
        'Authorization': 'Bearer ' + event['access_token']
    }
    if 'fields' in event:
        fields = event['fields']

    else:
        fields = []
        url = event['uri'] + '/services/data/v40.0/sobjects/' + event['sobject_name'] + '/describe'

        describe_object = requests.get(url, headers=headers)

        if 'error' in describe_object:
            return {
                'error': describe_object['error_description']
            }
        for field in describe_object['fields']:
            fields.append(field['name'])

    query = 'SELECT+'
    for (i, field) in enumerate(fields):
        if i == 0:
            query += field
        else:
            query += ',' + field

    query += '+FROM+' + event['sobject_name']

    url = event['uri'] + '/services/data/v40.0/query/q=' + query
    response = requests.get(url, headers=headers)
    if 'error' in response:
        return {
            'error': response['error_description']
        }
    return response



