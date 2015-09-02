---
title: DroneKit-Cloud

language_tabs:
  - python


toc_footers:
  - <a href='https://cloud.dronekit.io/signup'>Sign Up for a Developer Key</a>
  - <a href='http://www.droneshare.com/#create'>Create an account on DroneShare</a>
  - <a href='http://github.com/tripit/slate'>Documentation Powered by Slate</a>


search: true
---

# Introduction

Welcome to DroneKit-Cloud, 3D Robotics' cloud API for drone management and control.

DroneKit-Cloud API v1 lets you store, share, and access vehicle and flight log information using simple REST APIs. We hope you will use it to build drone tracking web apps like [Droneshare](http://www.droneshare.com/), and as a source of useful data about worldwide drone usage.

This documentation provides the information you need to get started. It includes the instructions on how to get an API id/key used for authorisation, API reference docs, and code fragments showing how to call many of the endpoints using Python (displayed in the right-pane relative next to their associated documentation).

If need more help, the best places to ask questions are our [discussion list](https://groups.google.com/forum/#!forum/drone-platform) and [StackOverflow](http://stackoverflow.com/questions/tagged/dronekit-cloud).


## Get Started

> This code shows the format of a query URL (in this case to get all users), and the api_key parameters.
> API calls which create or modify records must additionally pass *DroneShare* userid and password as parameters.

```python
import requests

url=http://api.3drobotics.com/api/v1/users #url to get all users
r = requests.get(url,
    params = {"api_key": appid.appkey},  #Replace appid and appkey with the id/key from DroneKit.
    )
print 'Status code: %s' % r.status_code
print(r.text)
```

In order to use the API you will need to [sign up for a free API key](https://cloud.dronekit.io/signup) with the DroneKit-Cloud service. After logging into DroneKit you will find your *App ID* and *App Key* [at this link](https://cloud.dronekit.io/).

This key must be included in all requests (expressed in the format `app_id.your_app_key`) and grants permission to:

* read and update users
* create, update and read vehicles
* create, update and read missions (limited to 500 calls/month)

Requests that create/modify information on the service must also include a [DroneShare](http://www.droneshare.com/) user id and password (they will return HTTP 401 "You do not own this record" if no login details are provided). You can [create a free account on DroneShare here](http://www.droneshare.com/#create).

The API base url is `http://api.3drobotics.com/api/v1/` and the available endpoints are listed below.

Examples of how to use the API and authorise requests are shown on the right-pane (replace `app_key` with your own id and key).



## Examples

* The Python examples shown in this document can be downloaded from here [examples/dronecode_cloud_example_code_in_python.py](examples/dronecode_cloud_example_code_in_python.py)
  You you will need to have Python (2.7) installed and pass your api keys and droneshare password:
  `dronecode_cloud_example_code_in_python.py  -u droneshare_userid -p droneshare_password -a dronekit_appid -k dronekit_appkey`

* A complete example in CoffeeScript is available in the form of the [DroneShare Website source code](https://github.com/dronekit/droneshare). The most relevant file is [dapiServices.coffee](https://github.com/dronekit/droneshare/blob/master/src/scripts/services/dapiServices.coffee).






# /user - User operations

This API exposes operations for browsing and searching lists of users, and retrieving information about a single user.


## JSON Objects

This section contains Json objects returned or used by the /user API.

### UserJson

> The `UserJson` object has the following Model Schema:

```json
{
  "login": "",
  "password": "",
  "email": "",
  "fullName": "",
  "wantEmails": "",
  "groups": "",
  "oldPassword": "",
  "defaultViewPrivacy": {},
  "defaultControlPrivacy": {}
}
```

The `UserJson` object has the following parameters:

Parameter | Data Type | Required | Description
--------- | ------- | ------- | -----------
login | string | Y | The loginName for the account
password | string |  | The password for the account
email | string |  | Email address for the account
fullName | string |  | Full name for the new user
wantEmails | string |  | Whether or not the user wants to receive update emails
groups | string |  | The user's group membership.
oldPassword | string |  | The old/current password for the account when changing the password
defaultViewPrivacy | EnumVal |  | The view privacy setting
defaultControlPrivacy | EnumVal |  | The control privacy setting





## Show all users

```python
import requests

# apikey is appid.appkey
# baseurl is http://api.3drobotics.com/api/v1/'

def allusers(aPageSize=100,aPageOffset=0):
    # Get all users
    r = requests.get(options.baseurl + 'user',
		params = {"api_key": apikey, "page_offset":aPageOffset,"page_size": aPageSize},
        )
    print 'Status code: %s' % r.status_code
    print 'Number of users: %s' % len(r.json())
    pprint.pprint(r.json())

print "\nGet all users (pagesize:2, pageoffset:40"
allusers(aPageSize=2,aPageOffset=40)
```


> The endpoint returns JSON with this Model Schema:

```json
[
  {
    "login": "",
    "password": "",
    "email": "",
    "fullName": "",
    "wantEmails": "",
    "groups": "",
    "oldPassword": "",
    "defaultViewPrivacy": {},
    "defaultControlPrivacy": {}
  }
]
```

This endpoint lists all users stored by the service.


### HTTP Request

`GET /user`


### Query Parameters

The query parameters are:

Parameter | Parameter type | Data type | Description
--------- | ------- | ------- | -----------
page_offset| query | integer | If paging, the record # to start with (use 0 at start)
page_size| query | integer | If paging, the # of records in the page. The default and maximum page size is 100 records.
order_by| query | string | To get sorted response, the field name to sort on
order_dir| query | string | If sorting, the optional direction. either asc or desc




## Find user by id

```python
import requests

# apikey is appid.appkey
# baseurl is http://api.3drobotics.com/api/v1/'

def userbyid(aId):
    # Get user with specified id
    r = requests.get(options.baseurl + 'user' + '/' + aId,
		params = {"api_key": apikey}
        )
    print 'Status code: %s' % r.status_code
    pprint.pprint(r.json())


print "Get user by id: %s" % 'mrpollo'
userbyid('mrpollo')
```



> The endpoint returns JSON with this Model Schema:

```json
{
  "login": "",
  "password": "",
  "email": "",
  "fullName": "",
  "wantEmails": "",
  "groups": "",
  "oldPassword": "",
  "defaultViewPrivacy": {},
  "defaultControlPrivacy": {}
}
```

This endpoint returns the user object for a specific id (loginName).


### HTTP Request

`GET /user/{id}`


### Query Parameters

The query parameters are:

Parameter | Data Type | Parameter Type | Required | Description
--------- | ------- | ------- | ------- | -----------
id | string | path | Y | Id of user that needs to be fetched





## Get param in user

```python
import requests

# apikey is appid.appkey
# baseurl is http://api.3drobotics.com/api/v1/'

def userparambyid(aId,aParam):
    # Get param value for user with specified id
    r = requests.get(options.baseurl + 'user' + '/' + aId + '/' + aParam,
		params = {"api_key": apikey}
        )
    return r

print "fullName"
r=userparambyid('hamishwillee','fullName')
print 'Status code: %s' % r.status_code
print(r.text)
```


> The command returns the requested value as a JValue:

```json
{Hamish Willee}
```

This endpoint returns the value (`JValue`) of a specified parameter for a given user.


### HTTP Request

`GET /user/{id}/{param}`


### Query Parameters

The query parameters are:

Parameter | Data Type | Parameter Type | Required | Description
--------- | ------- | ------- | ------- | -----------
id | string | path | Y | Id of user that needs to be fetched
param | string | path | Y | The parameter to read from the object. This has returns valid values for ``fullName``, ``id``, ``emailVerified``, ``needNewPassword`` (other parameters return 404 and 500 errors).





# /mission - Mission operations

This command exposes operations for browsing and searching lists of missions, and retrieving a single mission.

## JSON Objects

### MissionJson

> The `MissionJson` object has the following Model Schema:

```json
{
  "id": 0,
  "notes": "",
  "viewPrivacy": {},
  "vehicleId": 0,
  "maxAlt": 0,
  "maxGroundspeed": 0,
  "maxAirspeed": 0,
  "maxG": 0,
  "flightDuration": 0,
  "latitude": 0,
  "longitude": 0,
  "softwareVersion": "",
  "softwareGit": "",
  "createdOn": "",
  "updatedOn": "",
  "summaryText": "",
  "mapThumbnailURL": "",
  "viewURL": "",
  "vehicleText": "",
  "userName": "",
  "userAvatarImage": "",
  "isLive": false
}
```

The `MissionJson` object has the following parameters:

Parameter | Data Type | Required | Description
--------- | ------- | ------- | -----------
id | integer | Y | The id for the mission
notes | string |  |
viewPrivacy | EnumVal |  |
vehicleId | integer |  |
maxAlt | number |  |
maxGroundspeed | number |  |
maxAirspeed | number |  |
maxG | number |  |
flightDuration | number |  |
latitude | number |  |
longitude | number |  |
softwareVersion | string |  |
softwareGit | string |  |
createdOn | string |  |
updatedOn | string |  |
summaryText | string |  |
mapThumbnailURL | string |  |
viewURL | string |  |
vehicleText | string |  |
userName | string |  |
userAvatarImage | string |  |
isLive | boolean |  |




## Show all missions

```python
import requests

# apikey is appid.appkey
# baseurl is http://api.3drobotics.com/api/v1/'

def allmissions(aPageSize=100,aPageOffset=0):
    # Get all users
    r = requests.get(options.baseurl + 'mission',
		params = {"api_key": apikey, "page_offset":aPageOffset,"page_size": aPageSize},
        )
    print 'Status code: %s' % r.status_code
    print 'Number of missions in page: %s' % len(r.json())
    pprint.pprint(r.json())

print "\nGet all missions (pagesize:5, pageoffset:30)"
allmissions(aPageSize=5,aPageOffset=30)
```


> The endpoint returns JSON with the [MissionJson](#missionjson) Model Schema:

```json
[
  {
    "id": 0,
    "notes": "",
    "viewPrivacy": {},
    "vehicleId": 0,
    "maxAlt": 0,
    "maxGroundspeed": 0,
    "maxAirspeed": 0,
    "maxG": 0,
    "flightDuration": 0,
    "latitude": 0,
    "longitude": 0,
    "softwareVersion": "",
    "softwareGit": "",
    "createdOn": "",
    "updatedOn": "",
    "summaryText": "",
    "mapThumbnailURL": "",
    "viewURL": "",
    "vehicleText": "",
    "userName": "",
    "userAvatarImage": "",
    "isLive": false
  }
]
```

This endpoint lists all missions on the service ([MissionJson](#missionjson)).


### HTTP Request

`GET /mission/`


### Query Parameters

The query parameters are:

Parameter | Data Type | Parameter Type | Required | Description
--------- | ------- | ------- | ------- | -----------
live | boolean | query |   | Live flights only
completed | boolean | query |   | Completed flights only
within | string | query |   | Flights within a specified GeoJSON polygon
page_offset| integer | query | If paging, the record # to start with (use 0 at start)
page_size| integer | query | If paging, the # of records in the page. The maximum (and default) page size is 100 records.
order_by| string | query | To get sorted response, the field name to sort on
order_dir| string |query  | If sorting, the optional direction. either asc or desc



## Create new mission with auto-ID

```python

```


> The command returns a string:

```json
{
}
```

This endpoint creates new mission that will be given a dynamically constructed ID.


### HTTP Request

`PUT /mission/`


### Query Parameters

> The Json Model Schema for the body parameter ([MissionJson](#missionjson)) is:

```json
{
  "id": 0,
  "notes": "",
  "viewPrivacy": {},
  "vehicleId": 0,
  "maxAlt": 0,
  "maxGroundspeed": 0,
  "maxAirspeed": 0,
  "maxG": 0,
  "flightDuration": 0,
  "latitude": 0,
  "longitude": 0,
  "softwareVersion": "",
  "softwareGit": "",
  "createdOn": "",
  "updatedOn": "",
  "summaryText": "",
  "mapThumbnailURL": "",
  "viewURL": "",
  "vehicleText": "",
  "userName": "",
  "userAvatarImage": "",
  "isLive": false
}
```

The query parameters are:

Parameter | Data Type | Parameter Type | Required | Description
--------- | ------- | ------- | ------- | -----------
body | [MissionJson](#missionjson) | body | Y | The mission parameters





## Get recent flights for global map

```python
import requests

# apikey is appid.appkey
# baseurl is http://api.3drobotics.com/api/v1/'

def recentmissions():
    # Get recent missions in format suitable for global map view
    r = requests.get(options.baseurl + 'mission/staticMap',
		params = {"api_key": apikey}
        )
    print 'Status code: %s' % r.status_code
    pprint.pprint(r.json())
    print len(r.json()['updates'])

print "\nGet gets recent mission in format suitable for a global map view."
recentmissions()
```



> The endpoint returns JSON with the [MissionJson](#missionjson) Model Schema:

```json
[
  {
    "id": 0,
    "notes": "",
    "viewPrivacy": {},
    "vehicleId": 0,
    "maxAlt": 0,
    "maxGroundspeed": 0,
    "maxAirspeed": 0,
    "maxG": 0,
    "flightDuration": 0,
    "latitude": 0,
    "longitude": 0,
    "softwareVersion": "",
    "softwareGit": "",
    "createdOn": "",
    "updatedOn": "",
    "summaryText": "",
    "mapThumbnailURL": "",
    "viewURL": "",
    "vehicleText": "",
    "userName": "",
    "userAvatarImage": "",
    "isLive": false
  }
]
```

This endpoint gets recent flights suitable for a global map view.


### HTTP Request

`GET /mission/staticMap`




## Add a new mission

```python

```


> The endpoint returns JSON with the [MissionJson](#missionjson) Model Schema:

```json
[
  {
    "id": 0,
    "notes": "",
    "viewPrivacy": {},
    "vehicleId": 0,
    "maxAlt": 0,
    "maxGroundspeed": 0,
    "maxAirspeed": 0,
    "maxG": 0,
    "flightDuration": 0,
    "latitude": 0,
    "longitude": 0,
    "softwareVersion": "",
    "softwareGit": "",
    "createdOn": "",
    "updatedOn": "",
    "summaryText": "",
    "mapThumbnailURL": "",
    "viewURL": "",
    "vehicleText": "",
    "userName": "",
    "userAvatarImage": "",
    "isLive": false
  }
]

```

This endpoint adds a new mission as a tlog, bog or log.

The endpoint is designed to facilitate easy log file uploading from GCS applications. It requires no oauth or other authentication (but you will need to use your application's api_key). You should pass in the user's login and password as query parameters.

You'll also need to pick a UUID to represent the vehicle (if your user interface allows the user to specify particular models you should associate the UUID with the model - alternatively you can open a WebView and use droneshare to let the user pick a model). If the vehicle has not previously been seen it will be created.

If you are taking advantage of the autoCreate feature, you should specify a user email address and name (so we can send them password reset emails if they forget their password).

Both multi-part file POSTs and simple posts of log files as the entire request body are supported. In the latter case the content type must be set appropriately.


### HTTP Request

`POST /mission/upload/{vehicleUUID}`


### Query Parameters

The query parameters are:

Parameter | Data Type | Parameter Type | Required | Description
--------- | ------- | ------- | ------- | -----------
file | body | file | Y | log file as a standard html form upload POST
vehicleUUID | string | path | Y | UUID of vehicle to be have mission added (the client should pick a stable UUID)
login | string | query | Y | User login (used if not already logged-in via cookie)
password | string | query | Y | User password (used if not already logged-in via cookie)
email | string | query |  | Email address (optional, used if user creation is required)
fullName | string | query |  | User full name (optional, used if user creation is required)
autoCreate | boolean | query |  | If true a new user account will be created if required
privacy | string | query |  | The privacy setting for this flight (DEFAULT, PRIVATE, PUBLIC, SHARED, RESEARCHER)


### Error codes

HTTP Status Code | Reason
--------- | -------
200	Success | Payload will be a JSON array of mission objects. You probably want to show the user the viewURL for each file, but the other mission fields might also be interesting.




## Find by id

```python
import requests

# apikey is appid.appkey
# baseurl is http://api.3drobotics.com/api/v1/'

def missionbyid(aId):
    # Get mission with specified id
    r = requests.get(options.baseurl + 'mission' + '/' + aId,
		params = {"api_key": apikey}
        )
    print 'Status code: %s' % r.status_code
    pprint.pprint(r.json())

print "\nGet specified mission by id:(3)"
missionbyid('3')
```


> The endpoint returns JSON with the [MissionJson](#missionjson) Model Schema:

```json
{
  "id": 0,
  "notes": "",
  "viewPrivacy": {},
  "vehicleId": 0,
  "maxAlt": 0,
  "maxGroundspeed": 0,
  "maxAirspeed": 0,
  "maxG": 0,
  "flightDuration": 0,
  "latitude": 0,
  "longitude": 0,
  "softwareVersion": "",
  "softwareGit": "",
  "createdOn": "",
  "updatedOn": "",
  "summaryText": "",
  "mapThumbnailURL": "",
  "viewURL": "",
  "vehicleText": "",
  "userName": "",
  "userAvatarImage": "",
  "isLive": false
}
```

This endpoint returns the mission ([MissionJson](#missionjson)) for a specified id.

### HTTP Request

`GET /mission/{id}`


### Query Parameters

The query parameters are:

Parameter | Data Type | Parameter Type | Required | Description
--------- | ------- | ------- | ------- | -----------
id | string | path | Y | Id of mission that needs to be fetched






## Update by id

```python

```



This endpoint updates a specified mission with new values.


### HTTP Request

`PUT /mission/{id}`


### Query Parameters

> The Json Model Schema for the body parameter ([MissionJson](#missionjson)) is:

```json
{
  "id": 0,
  "notes": "",
  "viewPrivacy": {},
  "vehicleId": 0,
  "maxAlt": 0,
  "maxGroundspeed": 0,
  "maxAirspeed": 0,
  "maxG": 0,
  "flightDuration": 0,
  "latitude": 0,
  "longitude": 0,
  "softwareVersion": "",
  "softwareGit": "",
  "createdOn": "",
  "updatedOn": "",
  "summaryText": "",
  "mapThumbnailURL": "",
  "viewURL": "",
  "vehicleText": "",
  "userName": "",
  "userAvatarImage": "",
  "isLive": false
}
```

The query parameters are:

Parameter | Data Type | Parameter Type | Required | Description
--------- | ------- | ------- | ------- | -----------
id | string | path | Y | Id of mission that needs to be updated
body | [MissionJson](#missionjson) | body | Y | Json object with mission information




## Delete by id

```python

```

This endpoint deletes the mission with the specified id.


### HTTP Request

`DELETE /mission/{id}`


### Query Parameters

The query parameters are:

Parameter | Data Type | Parameter Type | Required | Description
--------- | ------- | ------- | ------- | -----------
id | string | path | Y | Id of mission that needs to be deleted




## Create by id

```python

```



> The command returns a string:

```json

```

This endpoint creates a new mission object with a specified id.


### HTTP Request

`POST /mission/{id}`


### Query Parameters

> The Json Model Schema for the body parameter ([MissionJson](#missionjson)) is:

```json
{
  "id": 0,
  "notes": "",
  "viewPrivacy": {},
  "vehicleId": 0,
  "maxAlt": 0,
  "maxGroundspeed": 0,
  "maxAirspeed": 0,
  "maxG": 0,
  "flightDuration": 0,
  "latitude": 0,
  "longitude": 0,
  "softwareVersion": "",
  "softwareGit": "",
  "createdOn": "",
  "updatedOn": "",
  "summaryText": "",
  "mapThumbnailURL": "",
  "viewURL": "",
  "vehicleText": "",
  "userName": "",
  "userAvatarImage": "",
  "isLive": false
}
```

The query parameters are:

Parameter | Data Type | Parameter Type | Required | Description
--------- | ------- | ------- | ------- | -----------
id | string | path | Y | Id of mission that needs to be created
body | [MissionJson](#missionjson) | body | Y | Json object with mission information




## Get analysis.json by id

```python

```


> The endpoint returns JSON with this Model Schema:

```json
{
  "obj": [
    {
      "_1": {},
      "_2": {}
    }
  ]
}
```

> And this Model:

```json
JObject {
  obj (array[Tuple2[String, JValue]])
 }

Tuple2[String, JValue] {
  _1 (Object),
  _2 (Object)
}

Object {
}
```

This endpoint gets the **analysis.json** for the specified mission.


### HTTP Request

`GET /mission/{id}/analysis.json`


The query parameters are:

Parameter | Data Type | Parameter Type | Required | Description
--------- | ------- | ------- | ------- | -----------
id | string | path | Y | Id of mission to be read





## Get dseries by id

```python

```


> The endpoint returns JSON with this Model Schema:

```json
[
  {
    "obj": [
      {
        "_1": {},
        "_2": {}
      }
    ]
  }
]
```

> And this Model:

```json
JObject {
  obj (array[Tuple2[String, JValue]])
 }

Tuple2[String, JValue] {
  _1 (Object),
  _2 (Object)
}
Object {
 }
```

This endpoint gets the dseries for the specified mission.


### HTTP Request

`GET /mission/{id}/dseries`


### Query Parameters

The query parameters are:

Parameter | Data Type | Parameter Type | Required | Description
--------- | ------- | ------- | ------- | -----------
id | string | path | Y | Id of mission to be read




## Get messages.geo.json by id


```python

```


> The endpoint returns JSON with this Model Schema:

```json
[
  {
    "obj": [
      {
        "_1": {},
        "_2": {}
      }
    ]
  }
]
```

> And this Model:

```json
JObject {
  obj (array[Tuple2[String, JValue]])
 }

Tuple2[String, JValue] {
  _1 (Object),
  _2 (Object)
}
Object {
 }
```

This endpoint gets the **messages.geo.json** for the specified mission.


### HTTP Request

`GET /mission/{id}/messages.geo.json`


### Query Parameters

The query parameters are:

Parameter | Data Type | Parameter Type | Required | Description
--------- | ------- | ------- | ------- | -----------
id | string | path | Y | Id of mission to be read






## Get messages.gmaps.kmz by id

```python

```


> The command returns an `array[string]`


This endpoint gets the **messages.gmaps.kmz** for the specified mission.


### HTTP Request

`GET /mission/{id}/messages.gmaps.kmz`

### Query Parameters

The query parameters are:

Parameter | Data Type | Parameter Type | Required | Description
--------- | ------- | ------- | ------- | -----------
id | string | path | Y | Id of mission to be read





## Get messages.json by mission id

```python

```



> The endpoint returns JSON with this Model Schema:

```json
{
  "modelType": "",
  "messages": [
    {
      "t": 0,
      "typ": "",
      "fld": [
        ""
      ]
    }
  ]
}
```

> And this Model:

```json
MessageHeader {
  modelType (string),
  messages (array[MessageJson])
}

MessageJson {
  t (integer),
  typ (string),
  fld (array[string])
}
```

This endpoint gets the **messages.json** for the specified mission.


### HTTP Request

`GET /mission/{id}/messages.json`


### Query Parameters

The query parameters are:

Parameter | Data Type | Parameter Type | Required | Description
--------- | ------- | ------- | ------- | -----------
id | string | path | Y | Id of mission to be read





## Get messages.kml by id

```python

```



> The command returns an `array[string]`


This endpoint gets the **messages.kml** for the specified mission.


### HTTP Request

`GET /mission/{id}/messages.kml`


### Query Parameters

The query parameters are:

Parameter | Data Type | Parameter Type | Required | Description
--------- | ------- | ------- | ------- | -----------
id | string | path | Y | Id of mission to be read





## Get messages.kmz by id

```python

```


> The command returns an `array[string]`

This endpoint gets the **messages.kmz** for the specified mission.


### HTTP Request

`GET /mission/{id}/messages.kmz`


### Query Parameters

The query parameters are:

Parameter | Data Type | Parameter Type | Required | Description
--------- | ------- | ------- | ------- | -----------
id | string | path | Y | Id of mission to be read




## Get messages.tlog by id

```python

```


> The endpoint returns JSON with this Model Schema:

```json
{
  "status": {
    "code": 0,
    "message": ""
  },
  "body": {},
  "headers": [
    ""
  ]
}
```

> With this Model:

```json
ActionResult {
  status (ResponseStatus),
  body (Object),
  headers (array[string])
}

ResponseStatus {
  code (integer),
  message (string)
}

Object {
}
```

This endpoint gets the **messages.tlog** for the specified mission.


### HTTP Request

`GET /mission/{id}/messages.tlog`


### Query Parameters

The query parameters are:

Parameter | Data Type | Parameter Type | Required | Description
--------- | ------- | ------- | ------- | -----------
id | string | path | Y | Id of mission to be read





## Get parameters.complete by id

```python

```


> The command returns a string:

```json

```

This endpoint gets the **parameters.complete** for the specified mission.


### HTTP Request

`GET /mission/{id}/parameters.complete`


### Query Parameters

The query parameters are:

Parameter | Data Type | Parameter Type | Required | Description
--------- | ------- | ------- | ------- | -----------
id | string | path | Y | Id of mission to be read





## Get parameters.json by id

```python

```



> The endpoint returns JSON with this Model Schema:

```json
[
  {
    "id": "",
    "range": [
      {}
    ],
    "value": "",
    "doc": "",
    "rangeOk": false
  }
]
```

> With this model:

```json
ParameterJson {
  id (string),
  range (array[Object], optional),
  value (string),
  doc (string),
  rangeOk (boolean)
}

Object {
}
```

This endpoint gets the **parameters.jso**n for the specified mission.


### HTTP Request

`GET /mission/{id}/parameters.json`


### Query Parameters

The query parameters are:

Parameter | Data Type | Parameter Type | Required | Description
--------- | ------- | ------- | ------- | -----------
id | string | path | Y | Id of mission to be read




## Get parameters.share by id

```python

```


> The command returns a string:

```json

```

This endpoint gets the **parameters.share** for the specified mission.


### HTTP Request

`GET /mission/{id}/parameters.share`


### Query Parameters

The query parameters are:

Parameter | Data Type | Parameter Type | Required | Description
--------- | ------- | ------- | ------- | -----------
id | string | path | Y | Id of mission to be read




##  Get parameter from a mission

```python

```


> The endpoint returns JSON (`JValue`) with this Model Schema:

```json
{}
```

This endpoint gets a specific parameter from a given mission.


### HTTP Request

`GET /mission/{id}/{param}`


### Query Parameters

The query parameters are:

Parameter | Data Type | Parameter Type | Required | Description
--------- | ------- | ------- | ------- | -----------
id | string | path | Y | Id of mission that needs to be fetched
param | string | path | Y | The parameter to read from the object









# /vehicle - Vehicle operations

This command exposes operations for browsing and searching lists of vehicles, and retrieving single vehicles.

## JSON Objects

### VehicleJson

> The `VehicleJson` object has the following Model Schema:

```json
{
  "uuid": {
    "mostSigBits": 0,
    "leastSigBits": 0
  },
  "name": "",
  "id": 0,
  "userId": 0,
  "manufacturer": "",
  "vehicleType": "",
  "autopilotType": "",
  "viewPrivacy": {},
  "controlPrivacy": {},
  "missions": [
    {}
  ],
  "createdOn": "",
  "updatedOn": "",
  "summaryText": "",
  "userName": ""
}
```

The `VehicleJson` object has the following parameters:

Parameter | Data Type | Required | Description
--------- | ------- | ------- | -----------
uuid | UUID | |
name | string |  |
id | integer |  |
userId | integer |  |
manufacturer | string |  |
vehicleType | string |  |
autopilotType | string |  |
viewPrivacy | EnumVal |  |
controlPrivacy | EnumVal |  |
missions | array[JValue] |  |
createdOn | string |  |
updatedOn | string |  |
summaryText | string |  |
userName | string |  |


The `UUID` object has the following parameters:

Parameter | Data Type | Required | Description
--------- | ------- | ------- | -----------
mostSigBits | integer |  |
leastSigBits | integer |  |



## Show all vehicles

```python
import requests

# apikey is appid.appkey
# baseurl is http://api.3drobotics.com/api/v1/'

def allvehicles(aPageSize=100,aPageOffset=0):
    # Get all vehicles
    r = requests.get(options.baseurl + 'vehicle',
		params = {"api_key": apikey, "page_offset":aPageOffset,"page_size": aPageSize},
        )
    print 'Status code: %s' % r.status_code
    print 'Number of vehicles in page: %s' % len(r.json())
    pprint.pprint(r.json())

print "\nGet all vehicles (pagesize:5, pageoffset:3)"
allvehicles(aPageSize=5,aPageOffset=3)

```



> The endpoint returns JSON with the [VehicleJson](#vehiclejson) Model Schema:

```json
[
  {
    "uuid": {
      "mostSigBits": 0,
      "leastSigBits": 0
    },
    "name": "",
    "id": 0,
    "userId": 0,
    "manufacturer": "",
    "vehicleType": "",
    "autopilotType": "",
    "viewPrivacy": {},
    "controlPrivacy": {},
    "missions": [
      {}
    ],
    "createdOn": "",
    "updatedOn": "",
    "summaryText": "",
    "userName": ""
  }
]
```

This endpoint retrieves all vehicles.


### HTTP Request

`GET /vehicle/`


Parameter | Parameter type | Data type | Description
--------- | ------- | ------- | -----------
page_offset| query | integer | If paging, the record # to start with (use 0 at start)
page_size| query | integer | If paging, the # of records in the page. The default and maximum page_size is 100 records.
order_by| query | string | To get sorted response, the field name to sort on
order_dir| query | string | If sorting, the optional direction. either asc or desc





## Create a new object with auto-ID

```python
import requests

# apikey is appid.appkey
# baseurl is http://api.3drobotics.com/api/v1/'
# options.username and options.password are droneshare passwords that will own the vehicle

def create_vehicle():
    # Create a test vehicle.
    # Requires DroneShare username and password.
    r = requests.put(options.baseurl + 'vehicle',
        params = {"api_key": apikey, "login": options.username, "password":options.password},
        headers = {"content-type": "application/json"},
        data = '{ "name": "DELETEME - Test Vehicle", "vehicleType": "quadcopter",  "autopilotType": "apm", "summaryText": "This vehicle is added by example code" }'
		)
	return r

r = create_vehicle()
print r.status_code
print pprint.pprint(r.json())
```

This endpoint creates a new vehicle record with a dynamically constructed ID.

The request requires both api key and droneshare login parameters. It returns JSON object for the created record.


### HTTP Request

`PUT /vehicle/`


### Query Parameters

> The Json Model Schema for the body parameter ([VehicleJson](#vehiclejson)) is:

```json
{
  "uuid": {
    "mostSigBits": 0,
    "leastSigBits": 0
  },
  "name": "",
  "id": 0,
  "userId": 0,
  "manufacturer": "",
  "vehicleType": "",
  "autopilotType": "",
  "viewPrivacy": {},
  "controlPrivacy": {},
  "missions": [
    {}
  ],
  "createdOn": "",
  "updatedOn": "",
  "summaryText": "",
  "userName": ""
}
```

The query parameters are:

Parameter | Data Type | Parameter Type | Required | Description
--------- | ------- | ------- | ------- | -----------
body | [VehicleJson](#vehiclejson) | body | Y | The vehicle parameters.





## Find by id

```python
import requests

# apikey is appid.appkey
# baseurl is http://api.3drobotics.com/api/v1/'


def vehiclebyid(aId):
    # Get vehicle with specified id
    r = requests.get(options.baseurl + 'vehicle' + '/' + aId,
		params = {"api_key": apikey}
        )
    print 'Status code: %s' % r.status_code
    pprint.pprint(r.json())

print "\nGet specified vehicle by id:(3)"
vehiclebyid('3')
```


> The endpoint returns JSON with this Model Schema:

```json
{
  "uuid": {
    "mostSigBits": 0,
    "leastSigBits": 0
  },
  "name": "",
  "id": 0,
  "userId": 0,
  "manufacturer": "",
  "vehicleType": "",
  "autopilotType": "",
  "viewPrivacy": {},
  "controlPrivacy": {},
  "missions": [
    {}
  ],
  "createdOn": "",
  "updatedOn": "",
  "summaryText": "",
  "userName": ""
}
```

This endpoint gets a vehicle with the specified ID.

This is the "database" record ``id``, not the vehicle ``uuid``.


### HTTP Request

`GET /vehicle/{id}`


### Query Parameters

The query parameters are:

Parameter | Data Type | Parameter Type | Required | Description
--------- | ------- | ------- | ------- | -----------
id | string | path | Y | Id of vehicle that needs to be fetched





## Update by id

```python
import requests

# apikey is appid.appkey
# baseurl is http://api.3drobotics.com/api/v1/'
# options.username and options.password are droneshare passwords that own the vehicle


def updatevehiclebyid(aId):
    # Update vehicle with specified id
    # This example just renames the vehicle.
    r = requests.put(options.baseurl + 'vehicle' + '/' + aId,
        params = {"api_key": apikey, "login": options.username, "password":options.password},
        headers = {"content-type": "application/json"},
        data = '{ "name": "DELETEME - Test Vehicle WITH NEW NAME" }'
		)
    return r

r=updatevehiclebyid('a valid id')

```


This endpoint updates the information in the vehicle record with the specified id.


### HTTP Request

`PUT /vehicle/{id}`


### Query Parameters

> The Json Model Schema for the body parameter ([VehicleJson](#vehiclejson)) is:

```json
{
  "uuid": {
    "mostSigBits": 0,
    "leastSigBits": 0
  },
  "name": "",
  "id": 0,
  "userId": 0,
  "manufacturer": "",
  "vehicleType": "",
  "autopilotType": "",
  "viewPrivacy": {},
  "controlPrivacy": {},
  "missions": [
    {}
  ],
  "createdOn": "",
  "updatedOn": "",
  "summaryText": "",
  "userName": ""
}
```

The query parameters are:

Parameter | Data Type | Parameter Type | Required | Description
--------- | ------- | ------- | ------- | -----------
body | [VehicleJson](#vehiclejson) | body | Y | The vehicle parameters
id | string | path | Y | Id of vehicle that needs to be updated




## Delete by id

> This code fragment shows the Python call to delete a vehicle with a specific id.

```python
import requests

# apikey is appid.appkey
# baseurl is http://api.3drobotics.com/api/v1/'
# options.username and options.password are droneshare passwords that own the vehicle

def deletevehiclebyid(aId):
    # Delete vehicle with specified id
    r = requests.delete(options.baseurl + 'vehicle' + '/' + aId,
        params = {"api_key": apikey, "login": options.username, "password":options.password}
        )
    return r

r=deletevehiclebyid()

```


This endpoint deletes the vehicle with the specified id.


### HTTP Request

`DELETE /vehicle/{id}`


### Query Parameters

The query parameters are:

Parameter | Data Type | Parameter Type | Required | Description
--------- | ------- | ------- | ------- | -----------
id | string | path | Y | Id of vehicle that needs to be deleted.





## Create by id

```python

```


> The command returns a string:

```json

```

This endpoint creates a new vehicle with the specified id.


### HTTP Request

`POST /api/v1/vehicle/{id}`


### Query Parameters

> The Json Model Schema for the body parameter ([VehicleJson](#vehiclejson)) is:

```json
{
  "uuid": {
    "mostSigBits": 0,
    "leastSigBits": 0
  },
  "name": "",
  "id": 0,
  "userId": 0,
  "manufacturer": "",
  "vehicleType": "",
  "autopilotType": "",
  "viewPrivacy": {},
  "controlPrivacy": {},
  "missions": [
    {}
  ],
  "createdOn": "",
  "updatedOn": "",
  "summaryText": "",
  "userName": ""
}
```

The query parameters are:

Parameter | Data Type | Parameter Type | Required | Description
--------- | ------- | ------- | ------- | -----------
body | [VehicleJson](#vehiclejson) | body | Y | The vehicle parameters
id | string | path | Y | Id of vehicle that needs to be created





## Add a new mission

```python

```


> The endpoint returns JSON with the [VehicleJson](#vehiclejson) Model Schema:

```json
[
  {
    "uuid": {
      "mostSigBits": 0,
      "leastSigBits": 0
    },
    "name": "",
    "id": 0,
    "userId": 0,
    "manufacturer": "",
    "vehicleType": "",
    "autopilotType": "",
    "viewPrivacy": {},
    "controlPrivacy": {},
    "missions": [
      {}
    ],
    "createdOn": "",
    "updatedOn": "",
    "summaryText": "",
    "userName": ""
  }
]
```

This endpoint adds a new mission (as a tlog, bog or log).


### HTTP Request

`POST /vehicle/{id}/missions`


### Query Parameters

The query parameters are:

Parameter | Data Type | Parameter Type | Required | Description
--------- | ------- | ------- | ------- | -----------
file | file | body | Y | Log file as a standard html form upload POST
id | string | path | Y | Id of vehicle to be have mission added



