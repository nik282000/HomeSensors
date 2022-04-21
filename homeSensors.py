#!/usr/bin/env python3

import requests
from datetime import datetime
import pathlib

debug = True


def debug_print(message):
    if debug:
        print(message)


today = datetime.now().strftime('%Y_%m_%d')
now = datetime.now().strftime('%Y_%m_%d_%H:%M')
today_filename = '/var/homesensors/measurements/' + 'measurements_' + today + '.csv' # Change this line to where use Full Path

debug_print('Debug Print is ON.')
debug_print(today)
debug_print(now)
debug_print(today_filename)

sensor_list = [ # Adjust this list to include the name and IP addresses of your devices
    {
        'ip':'192.168.0.220',
        'name':'Sensor 0'
    },
    {
        'ip':'192.168.0.221',
        'name':'Sensor 1'
    },
    {
        'ip':'192.168.0.222',
        'name':'Sensor 2'
    },
    {
        'ip':'192.168.0.223',
        'name':'Sensor 3'
    }
]

for i in range(len(sensor_list)):
    try:
        raw = requests.get('http://' + sensor_list[i]['ip'], timeout=30) # Sensors should return temperature and humidity 'tt.tt,hh.hh'
        reading = raw.text.split(',')
    except: # If one of the sensors fails to respond use '0.0' as dummy data
        reading = ['0.0', '0.0']
        print(now + ' ' + sensor_list[i]['name'] + ' is missing.')
    sensor_list[i]['temperature'] = reading[0]
    sensor_list[i]['humidity'] = reading[1]

debug_print(sensor_list)

if pathlib.Path(today_filename).is_file() != True: # If measurements_yyyy_mm_dd.csv does not exist create a file for today
    debug_print("Today's file not found, creating file.")
    with open(today_filename, 'w+') as csv_file: # Create first line for csv file 'Datetime,sensor name0 temperature,sensor name0 humidity,...'
        title_line = 'Datetime'
        for i in range(len(sensor_list)):
            title_line = title_line + ',' + sensor_list[i]['name'] + ' temperature,' + sensor_list[i]['name'] + ' humidity'
        debug_print(title_line)
        csv_file.write(title_line + '\n')

with open(today_filename, 'a') as csv_file: # Create csv data line 'yyyy_mm_dd_hh:mm,s0 temp, s0 humi,s1 temp, s1 humi,...'
    csv_line = now
    for i in range(len(sensor_list)):
        csv_line = csv_line + ',' + sensor_list[i]['temperature'] + ',' + sensor_list[i]['humidity']
    debug_print(csv_line)
    csv_file.write(csv_line + '\n')

debug_print('Done.\n')
