# HomeSensors
Climate Monitoring with ESP8266

Super hacky way to monitor the temperature and humidity at home.

ESP8266_AHTx0.ino Runs on an ESP8266 with an AHT10 or AHT20 device conencted to it via I2c. It sits on a static IP on the network and hosts up a single line of text consisting of the temperature and humidity separated by a comma. eg. 12.3,45.6 This file is literally the ESP webserver demo sketch mashed up with the Adafruit_AHTX0 demo sketch. There is 100% a better way to do this.

homeSensors.py Reads from each sensor (listed in sensor_list) and then appends the data to a csv file /var/homesensors/measurements/measurements_YYYY_MM_DD.csv. If a csv for today doesn't exist it will be made. The first line will be labels for the columns: Datetime,SensorName0Temperature,SensorName0Humidity... If a sensor is unreachable or takes longer than 30s to respond the script will substitute 0.0,0.0 for the missing data and print a message. I append those messages to /var/homesensors/logs/errors but thats just me.

The file measurements_2022_01_22.csv is an example output from homeSensor.py for a whole day.
