
# Import libraries
import json
import requests
import time # Used to regulate poll frequency
import connectedcar # Client library for Ford Pass API
import os

poll_interval = 90 # seconds

def get_btc_price():
    # defining key/request url
    key = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
  
    # requesting data from url
    data = requests.get(key)  
    data = data.json()
    #print(f"{data['symbol']} price is {data['price']}")
    return float(data['price'])


def poll_for_price_change():
    # Get initial BTC price
    current_price = get_btc_price()
    time.sleep(poll_interval)

    while True:
        last_price = current_price
        current_price = get_btc_price()

        if current_price > last_price: # price increase
            difference = round(current_price - last_price, 2)
            print(f"BTC increased by ${difference} USD")
            return "increasing"
            
        elif current_price < last_price: # price decrease
            difference = round(last_price - current_price, 2)
            print(f"BTC decreased by ${difference} USD")
            return "decreasing"
        else: # No change, so keep wait then keep polling
            time.sleep(poll_interval)

    
def main():

    print("Starting bitcoin_light!")

    # Initialize Ford Connect
    # Set environment variables
    os.environ['API_USER'] = 'user'
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

    ford_transit_vin = vehicleList[0]
    ford_transit_vehicle = connectedcar.Vehicle(ford_transit_vin, access['access_token'])

    while True: # Loop forever
        price_state = poll_for_price_change() # Blocking call
        if price_state == "increasing":
            print(ford_transit_vehicle.start())
        elif price_state == "decreasing":
            print(ford_transit_vehicle.stop())
        else:
            print("Error while polling BTC price")

if __name__ == "__main__":
    main()