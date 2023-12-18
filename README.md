# UMR2toMQTT
Python routine to read out UMR2 floorheating controller and publish values to MQTT.

I created this routine to routinely readout my new WTH UMR2 floorheater control unit and publish variables via MQTT to my Home Assistant. The UMR2 controller publishes its status on a webpage via a json element. This routine calls the json and parses it to select specific parameters for publication. It also calculates the difference between the temperature floor in and floor out.

## Before use
Run the script 'UMR2toJSON' 1 time to identify the parameters you want publish on MQTT. Remember to first correct the IP-address of your UMR2 in the script. Use current values on the UMR2 status webpage to check values.
Once you have identified the correct parameters, adjust the script 'UMR2toMQTT' as necessary to publish the parameters you want.

## Running the script
Some parameters may need to be adjusted for your situation, like IP-addresses of the UMR2 and your MQTT server. Adjust as necessary in the script.
Depending on your deployment, you may need to adjust the environment. I am running the script on a Synology NAS as a user-script which is started once, at boot-up. Since DSM7 you have to run a Python script which calls modules as the user 'root' for it to access the Python modules.

## Home Assistant sensors
The values for the sensors published via MQTT will not automatically appear in Home Assistant. I have solved this by adding the text in the file 'HA-UMR2-sensors.yaml' in the HA 'configuration.yaml' file.

## Support
Support may be limited, feel free to amend the script as you like. This is my first script on GitHub ;-)

## Copyright
UMR2 is the controller manufactured by the Dutch floor heating company [WTH](https://www.wth.nl/).
I did not deconstruct any of the software on the UMR2, merely looked at the published webpage.
