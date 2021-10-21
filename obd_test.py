import obd  # used to communicate with vehicle
import time # used for sleep

connection = obd.OBD()
delay = 1


def print_stats():
    speedCmd = obd.commands.SPEED  # select an OBD command (sensor)
    response = connection.query(speedCmd)  # send the command, and parse the response
    speed = str(response.value.to("mph").magnitude)

    rpmCmd = obd.commands.RPM
    response = connection.query(rpmCmd)
    rpm = response.value.magnitude

    throttleCmd = obd.commands.THROTTLE_POS
    response = connection.query(throttleCmd)
    throttle = str(response.value.magnitude)

    runTimeCmd = obd.commands.RUN_TIME
    response = connection.query(runTimeCmd)
    runTime = str(response.value)

    fuelLevelCmd = obd.commands.FUEL_LEVEL
    response = connection.query(fuelLevelCmd)
    fuel_level = str(response.value)

    data = {'speed': speed, 'rpm': rpm, 'throttle': throttle, 'runTime': runTime, 'fuel_level': fuel_level}
    print(data)

def print_dtc():
    dtcCmd = obd.commands.GET_DTC
    response = connection.query(dtcCmd)
    dtcCodes = response.value

    print('dtcCodes: ', dtcCodes)

def main():
    print("protocol id: ", connection.protocol_id())  # 6 = ISO 15765-4 (CAN 11/500)

    while True:
        #print_stats()
        print_dtc()
        time.sleep(delay)


if __name__ == "__main__":
    main()