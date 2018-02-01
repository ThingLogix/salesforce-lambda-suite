# ThingLogix  
#### Salesforce Suite for Python & AWS Lambda   

## Installation Guide  

You will first need to clone this repository to your device.  You can do this from this git hub page by clicking the green
'clone or download' button found on the right side of the screen and clicking 'download as zip'.<br>

Sign into your AWS account and navigate to the AWS Lambda page, this can be found from the console by clicking the
'Lambda' button under the 'Compute' section.<br>

<b>You will need to do each of the following installation steps for each of the lambda functions in this suite</b>

Click the 'Create Function' button in the upper right.<br>

Under 'Author from scratch', make sure that you have each of the following:
- Name can be anything you want
- Runtime must be 'Python 3.6'
- Role must be 'Choose an existing role'
- In the 'Existing role' drop down menu, select 'lambda_basic_execution'

Go ahead and create your lambda function by clicking the orange button in the bottom right corner

In the lambda configuration screen scroll down to the page the says 'Function Code'
in the 'Code Entry Type' drop down, select 'Upload a .ZIP file'

In the 'Handler' menu, type the appropriate handler for the function you are currently creating:
<table>
     <tr>
         <th> Lambda Name </th>
         <th> Handler <b>(type this)</b> </th>
     </tr>
     <tr>
         <td> refresh_access_token </td>
         <td> refresh_access_token.lambda_handler</td>
     </tr>
     <tr>
         <td> get_metadata </td>
         <td> get_metadata.lambda_handler</td>
     </tr>
     <tr>
         <td> update_sf_record </td>
         <td> update_sf_record.lambda_handler</td>
    </tr>
    <tr>
        <td> get_records_for_sf_object </td>
        <td> get_records_for_sf_object.lambda_handler</td>
    </tr>
</table>
    

The last step is to upload code.  Unzip the folder that you just downloaded.  Inside navigate to the lambdas folder.  You will need to zip each of these files individually by right clicking, hovering over "send to", and selecting "zipped folder".
Under the function package section, select "Upload" and select the zip for the respective lambda that you are currently working on.

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
}
```
**uri**: the instance url of your org. All of this info can be obtained by calling *refresh_access_token*

### update_sf_record
This lambda function is responsible for updating a single Salesforce object 

The parameters are as follows:
```
{
    "access_token": String 
    "uri": String
    "sobject_id": String
    "sobject_name": String
    "attributes": Json Object
}   
```

### get_records_for_sf_object
This lambda function retrieves all objects associated with a particular Salesforce Objects

The parameters are as follows:
```
{
    "access_token": String 
    "uri": String
    "sobject_name": String
    "fields": (optional) List
}   
```

