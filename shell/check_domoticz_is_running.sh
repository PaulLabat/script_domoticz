#!/bin/sh
# check domoticz
status=`curl -s -i -H "Accept: application/json" "http://192.168.0.102:8080/json.htm?type=devices&rid=1" | grep "status"| awk -F: '{print $2}'|sed 's/,//'| sed 's/\"//g'`
if [ $status ]
then
	echo "Domoticz has already been started"
else
	sudo service domoticz.sh stop
	sleep 5
	sudo service domoticz.sh start
	#date "+- redemarre le %d/%m/%y a %H:%M:%S" >> /media/usb1/check_domoticz_online.log
fi
