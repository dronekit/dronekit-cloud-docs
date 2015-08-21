"""
This example code demonstrates how to use the DroneKit-Cloud API with Python.
"""

#for options parsing
from optparse import OptionParser
import pprint
import time
import requests


#parser options
parser = OptionParser(version="%prog 0.1.1", usage="Usage: %prog [options] version")
parser.add_option("-a", "--appid", dest="appid", default="89b511b1", help="App ID - default is example")
parser.add_option("-k", "--appkey", dest="appkey", default="d884d1cb57306e63925fcc07d032f2af",help="App key - default is example")
parser.add_option("-u", "--username", dest="username", default="",help="Droneshare username")
parser.add_option("-p", "--password", dest="password", default="",help="Droneshare password")
#parser.add_option("-b", "--baseurl", dest="baseurl", default="http://api.droneshare.com/api/v1/",help="Droneshare password")
parser.add_option("-b", "--baseurl", dest="baseurl", default="http://api.3drobotics.com/api/v1/",help="Droneshare password")
(options, args) = parser.parse_args()

print "App ID: %s" % options.appid
print "App key: %s" % options.appkey
print "Droneshare UserId: %s" % options.username
print "Droneshare Password: %s" % options.password
print "Base URL: %s" % options.baseurl
apikey=options.appid+'.'+options.appkey


if not (options.username and options.password):
   print "Username or Password not set. Examples that create/modify records will not be run."




########################################################################################
# User Operations
########################################################################################

def userbyid(aId):
    # Get user with specified id
    r = requests.get(options.baseurl + 'user' + '/' + aId, 
		params = {"api_key": apikey}
        )
    return r


username='hamishwillee'
print "Get user by id: %s" % username
r=userbyid(username)
print 'Status code: %s' % r.status_code
pprint.pprint(r.json())


def userparambyid(aId,aParam):
    # Get specified parameter for user with specified id
    r = requests.get(options.baseurl + 'user' + '/' + aId + '/' + aParam, 
		params = {"api_key": apikey}
        )
    return r

parameter='fullName'
print "Value of parameter %s in user %s" % (username,parameter)
r=userparambyid(username,parameter)
print 'Status code: %s' % r.status_code
print(r.text)



def allusers(aPageSize=100,aPageOffset=0):
    # Get all users
    r = requests.get(options.baseurl + 'user', 
		params = {"api_key": apikey, "page_offset":aPageOffset,"page_size": aPageSize},
        )
    print 'Status code: %s' % r.status_code
    print 'Number of users in page: %s' % len(r.json())
    pprint.pprint(r.json())
	
print "\nGet all users (pagesize:2, pageoffset:40)"	
allusers(aPageSize=2,aPageOffset=40)


########################################################################################
# Mission Operations
########################################################################################

def missionbyid(aId):
    # Get mission with specified id
    r = requests.get(options.baseurl + 'mission' + '/' + aId, 
		params = {"api_key": apikey}
        )
    print 'Status code: %s' % r.status_code
    pprint.pprint(r.json())

print "\nGet specified mission by id:(3)"	
missionbyid('3')


def allmissions(aPageSize=100,aPageOffset=0):
    # Get all missions
    r = requests.get(options.baseurl + 'mission', 
		params = {"api_key": apikey, "page_offset":aPageOffset,"page_size": aPageSize},
        )
    print 'Status code: %s' % r.status_code
    print 'Number of missions in page: %s' % len(r.json())
    pprint.pprint(r.json())
	
print "\nGet all missions (pagesize:5, pageoffset:30)"	
allmissions(aPageSize=5,aPageOffset=30)



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



########################################################################################
# Vehicle Operations
########################################################################################

def vehiclebyid(aId):
    # Get vehicle with specified id
    r = requests.get(options.baseurl + 'vehicle' + '/' + aId, 
		params = {"api_key": apikey}
        )
    print 'Status code: %s' % r.status_code
    pprint.pprint(r.json())

print "\nGet specified vehicle by id:(3)"	
vehiclebyid('3')



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


def create_vehicle():
    # Create a test vehicle
    r = requests.put(options.baseurl + 'vehicle',
        params = {"api_key": apikey, "login": options.username, "password":options.password},
        headers = {"content-type": "application/json"},
        data = '{ "name": "DELETEME - Test Vehicle", "vehicleType": "quadcopter", "autopilotType": "apm", "summaryText": "This vehicle is added by example code" }'
		)
    return r




# Test code showing how to delete vehicles	

if options.username and options.password:
    #Create vehicle if have dronehare account
    print 'Create test vehicle'
    r = create_vehicle()
    print r.status_code
    print pprint.pprint(r.json())
    print "See vehicle in user object"
    r=userbyid(options.username)		
    print 'Status code: %s' % r.status_code
    pprint.pprint(r.json())


def deletelastvehicleforuser(aId):
    # Deletes the last vehicle created by the user IFF its name starts with 'DELETEME'.
    r=userbyid(aId)
    try:
        last_vehicle=r.json()['vehicles'][-1]
        if last_vehicle['name'].startswith('DELETEME'):
            print "Deleting vehicle: %s" % last_vehicle['name']
            deletevehiclebyid('%s' % last_vehicle['id'])           
    except:
        print "Last vehicle cannot be deleted"


def deletevehiclebyid(aId):
    # Delete vehicle with specified id
    r = requests.delete(options.baseurl + 'vehicle' + '/' + aId, 
        params = {"api_key": apikey, "login": options.username, "password":options.password}
        )
    return r

	
if options.username and options.password:
    #Delete vehicle if have dronehare account and if last vehicle was created by test code 
    print 'Deleting last vehicle added by: %s' % options.username
    r=deletelastvehicleforuser(options.username)

	

	
# Test code showing how to update vehicles	

def updatelastvehicleforuser(aId):
    # Update vehicle created by the user IFF its name starts with 'DELETEME'.
    r=userbyid(aId)
    try:
        last_vehicle=r.json()['vehicles'][-1]
        if last_vehicle['name'].startswith('DELETEME'):
            print "Deleting vehicle: %s" % last_vehicle['name']
            updatevehiclebyid('%s' % last_vehicle['id'])           
    except:
        print "Last vehicle cannot be updated"

	
def updatevehiclebyid(aId):
    # Update vehicle with specified id
    r = requests.put(options.baseurl + 'vehicle' + '/' + aId,
        params = {"api_key": apikey, "login": options.username, "password":options.password},
        headers = {"content-type": "application/json"},
        data = '{ "name": "DELETEME - Test Vehicle WITH NEW NAME" }'
		)
    return r

if options.username and options.password:
    #Update vehicle if have dronehare account and if last vehicle was created by test code 
    print 'Create test vehicle'
    r = create_vehicle()
    print r.status_code
    print 'Updating name of last vehicle added by: %s' % options.username
    print 'The name of the vehicle will be changed to: "DELETEME - Test Vehicle WITH NEW NAME"'
    r=updatelastvehicleforuser(options.username)

	
