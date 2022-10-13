

import os # Used to load/set credentials from environment variable
import connectedcar # Client library for Ford Pass API

# Set environment variables
os.environ['API_USER'] = 'username'
os.environ['API_PASSWORD'] = 'secret'

# Get environment variables
USER = os.getenv('API_USER')
PASSWORD = os.environ.get('API_PASSWORD')
#print(USER, PASSWORD)

# get API token
client = connectedcar.AuthClient('9fb503e0-715b-47e8-adfd-ad4b7770f73b', None, None, None, 'US') # Region argument is only required if you live outside the United States.
access = client.get_user_access_token(USER, PASSWORD)
user = connectedcar.User(access['access_token'], "US") # Region argument is only required if you live outside the United States.


# Fetch some data
vehicles = user.vehicles()

vehicleList = [] # Array of vehicles



for userVehicle in vehicles: # For each user vehicle
    vehicleList.append(userVehicle['vin'])
    ford_transit = userVehicle

print(vehicleList)
print(user.info())

ford_transit_vin = vehicleList[0]
ford_transit_vehicle = connectedcar.Vehicle(ford_transit_vin, access['access_token'])

print(ford_transit_vehicle.odometer())
#print(ford_transit_vehicle.stop())