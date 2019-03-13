## santet-online 08-03-2018 (12:12)
# -*- coding: utf-8 -*-
# BlackHole Security
##
import time
from core.misc import *
from core.onlen import *

clearscreen()
logo()
print """
Seleccione una Opcion:
  01) Crear un Netcat Payload y Listener
  02) Ataque y Secuestro de Grupo de FaceBook
  03) Vectores de Ataque de Bombardeo SMS
  04) SMS Spoof Attack Vectors
  05) Ataque de Denegacion de Servicio
  
  00) Salir de Santet
"""
santet = raw_input("santet > ")

if santet == "01" or santet == "1":
	netcat_rat()
elif santet == "02" or santet == "2":
	facebookgroup_hijack()
elif santet == "03" or santet == "3":
	sms_bomber_jdid()
elif santet == "04" or santet == "4":
	sms_spoof_elk()
elif santet == "05" or santet == "5":
	denialofservice_attack()
else:
	print "\nERROR: Entrada Incorrecta..."
	time.sleep(2)
	restart_program()
