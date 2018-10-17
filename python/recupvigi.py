#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
import os
import json
import requests

#28/01/2015 : ajout codage utf8


############# Parametres ################################# 

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# les parametres de Domoticz
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

domoticz_ip='192.168.0.102'
domoticz_port='8080'

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# les IDX des switch "Alerte"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# soit 3 widget differents
# une pour l'etat des crues
# une pour la couleur generale de l'alerte
# une pour le type de risque 'orage,pluie,inondation,neige ....'
# remplacer les 116,124,125 p&r vos idx de vos alertes

# soit que  2 widget alert 
# un pour crues
#l'autre pour la couleur ET le risque dans le  meme
# on peut mettre couleur_vigilance et risk sur le meme idx qui contiendra donc a la fois le texte et la couleur

periph_idx={'crues': 62,
            'couleur_vigilance' : 61,
            'risk' : 61,
		'alerteSwitch' : 70}

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# associer ici les couleurs des alertes meteofrance aux couleurs de Domoticz
# rappel des couleurs Domoticz  0=gris, 1=vert,2=jaune,3=orange,4=rouge
# meteofrance envoie RAS qui ici est asscocie a gris
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

dict_couleur_widget_texte={'RAS' : 0,
			   'vert' : 1,
			   'jaune': 2,
			   'orange' : 3,
			   'rouge' : 4
			  }
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# les parametres de meteofrance
# on passe le numero du departemeznt en appelant le script
# sinon supprimer ces lignes et decommenter Departement=
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#if len(sys.argv) ==1:
#    print "Donner un departement"
#    sys.exit(0)
#
#else:
#    Departement =sys.argv[1]


Departement='78'


dict_text_vigilance = {
	'RAS':'Rien',
	'vert':'Pas de vigilance',
	'jaune':'Risque de crue',
	'orange':'Risque de crue importantes',
	'rouge':'Risque de crue majeure'
}


###############  fin des parametres #############################



r = requests.get('http://domogeek.entropialux.com/vigilance/'+Departement+'/all')
status=r.status_code

if status == 200:
# l'API renvoie 200 si tout est OK
   # print "Recup OK"

     # vigijson est un dict au sens python
    vigijson=r.json()
    # print vigijson
     #extraire les valeurs du dict avec les cles vigilanceflood,vigilancecolor et risk
    crues = vigijson['vigilanceflood']
     # on recupere la couleur associe au risque que l'on vient de trouver dans le dict des couleurs
    couleur_crues=str(dict_couleur_widget_texte[crues])
    text_crue = dict_text_vigilance[crues]
    
     # composons l'url
     # aller trouver l'idx des crues
    domoticz_idx=str(periph_idx['crues'])
    url_domoticz='http://'+domoticz_ip+':'+domoticz_port+'/json.htm?type=command&param=udevice&idx='+domoticz_idx+'&nvalue='+couleur_crues+'&svalue='+text_crue
    #  print url_domoticz

    r=requests.get(url_domoticz)
    if  r.status_code != 200:
        print "Erreur API"
    #
     # idem
    couleur_vigilance = vigijson['vigilancecolor']
    
     # on recupere la couleur associe au risque que l'on vient de trouver dans le dict des couleurs
    couleur_gen=str(dict_couleur_widget_texte[couleur_vigilance])
    
    # composons l'url
    # aller trouver l'idx des vigilances
    domoticz_idx=str(periph_idx['couleur_vigilance'])
    url_domoticz='http://'+domoticz_ip+':'+domoticz_port+'/json.htm?type=command&param=udevice&idx='+domoticz_idx+'&nvalue='+couleur_gen+'&svalue='+couleur_vigilance
    # print url_domoticz

    r=requests.get(url_domoticz)
    if  r.status_code != 200:
        print "Erreur API"

     # risk contient un texte d'explication ('neige','pluie',etc...)
    risk  = vigijson['vigilancerisk']
    if risk=="RAS":
        couleur_risk=dict_couleur_widget_texte[risk]
	message_risk=risk
    else: 
        message_risk=risk
	couleur_risk='4'
    
     # composons l'url
     #  si le message est RAS la coueleur est gris
     # on recupere un message texte neige pluie ... dans message_risk , la couelur est celle de couleur_gen 
    domoticz_idx=str(periph_idx['risk'])
    url_domoticz='http://'+domoticz_ip+':'+domoticz_port+'/json.htm?type=command&param=udevice&idx='+domoticz_idx+'&nvalue='+couleur_gen+'&svalue='+risk
    r=requests.get(url_domoticz)
    if  r.status_code != 200:

        print "Erreur API"

    mailLevel = 0
    if int(couleur_gen) == 2:
	mailLevel = 10
    elif int(couleur_gen) == 3:
        mailLevel = 20
    elif int(couleur_gen) == 4:
        mailLevel = 30

    domoticz_idx = str(periph_idx['alerteSwitch'])
    url_domoticz = 'http://'+domoticz_ip+':'+domoticz_port+'/json.htm?type=command&param=switchlight&idx='+domoticz_idx+'&switchcmd=Set%20Level&level='+str(mailLevel)
    r=requests.get(url_domoticz)
    if  r.status_code != 200:
        print "Erreur API"

  #  print crues,couleur_vigilance,risk,message_risk
  #  print couleur_crues,couleur_gen,couleur_risk

else:
    print "Erreur API"
