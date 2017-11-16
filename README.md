# ThingLogix  
#### Salesforce Suite for Python & AWS Lambda   

## Installation Guide

Clone this repository and zip its contents. Then upload each of the lambda functions as separate entities, or as 
individual components. 

## Lambdas  
### refresh_access_token  

This Lambda function is responsible for refreshing an access token and returning it to the user so that you can 
continue with an OAuth flow.  

The parameters are as follows: 
```
{
    "refresh_token": String,
    "client_id": String,
    "client_secret": String
}

```
You can find your client id and secret in Salesforce.

### get_metadata
This Lambda function is responsible for getting all of the metadata associated with an org in Salesforce. 

The parameters are as follows: 
```
{
    "access_token": String,
    "client_id": String,
    "client_secret": String,
    "uri": String
```
**uri**: the instance url of your org. All of this info can be obtained by calling *refresh_access_token*