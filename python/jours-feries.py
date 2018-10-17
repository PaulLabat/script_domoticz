#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import json
import requests

domoticz_ip='192.168.0.102'
domoticz_port='8080'

IDX = '111'

r = requests.get('http://domogeek.entropialux.com/holiday/now/json')
status=r.status_code

if status == 200:
# l'API renvoie 200 si tout est OK
    isFerie = "0"
    res = r.json()['holiday']
    if res == "Saint-Etienne (Alsace)":
	isFerie = '0'
    elif res != "False":
        isFerie = '10'

    url_domoticz='http://'+domoticz_ip+':'+domoticz_port+'/json.htm?type=command&param=switchlight&idx='+IDX+'&switchcmd=Set%20Level&level='+isFerie

    r=requests.get(url_domoticz)
    if  r.status_code != 200:
        print "Erreur API"
    
else:
    print "Erreur API"

