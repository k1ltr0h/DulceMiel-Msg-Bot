import requests
import time
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
#import vlc
from pygame import mixer  # Load the popular external library
from twilio.rest import Client

load_dotenv(verbose=True)
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
MY_WSP = os.getenv("MY_WSP")
TWILIO_WSP = os.getenv("TWILIO_WSP")

# las credenciales son leídas desde las variables de entorno TWILIO_ACCOUNT_SID y AUTH_TOKEN
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
# este es el número de testeo de Twilio sandbox sandboxtfrom_whatsapp_number='whatsapp:+14155238886'
# reemplace este número con su numero personal de whastapp, to_whatsapp_number='whatsapp:+15005550006'

# Iniciar mixer
mixer.init()
dj = mixer.music
#dj.load('Super_Mario_Land_Ending.mp3')
#wait = vlc.MediaPlayer("Super_Mario_Land_Ending.mp3")

r = requests.get('https://www.dulcemiel.com')
#print(r.text)
soup = BeautifulSoup(r.text, "html.parser")
#print(soup.prettify())

tmp_msj = "" #Evita que se re-envien los mensajes

while True:
	try:
		r = requests.get('https://www.dulcemiel.com')
		soup = BeautifulSoup(r.text, "html.parser")
		msg = soup.find("h2").string

		if(msg) == "Abriendo pronto":
			print(msg)
		else:
			open_shop = soup.find("div", class_="announcement--text font--accent").string
			print(open_shop.split)
			print("La pág se ha actualizado!!! o.o" + str(open_shop))
			if open_shop != tmp_msj:
				client.messages.create(body='Algo ha cambiado o.o, revisa la página! ' + str(open_shop),
						from_=TWILIO_WSP,
						to=MY_WSP)
				if open_shop.split()[1] == "¡¡Pronto!!":
					dj.load('were-ready-master_im-not-ready.mp3')
					dj.play()
				else:
					dj.load('Super_Mario_Land_Ending.mp3')
					dj.play()
				tmp_msj = open_shop
			time.sleep(5)
	except:
		print("Algo raro pasó o.o, revisa la pag! o presionaste Ctrl+c para salir e.e")
		dj.load('were-ready-master_im-not-ready.mp3')
		dj.play()
		try:
			client.messages.create(body='Revisa la página!, si no ves nada nuevo, quizá se ha caído la red o algún problema con el Bot. Pero tranquila, se volverá a activar en 1 minuto.',
						from_=TWILIO_WSP,
						to=MY_WSP)
		except:
			print("Creo que se ha caído la conexión a internet D;")	
		time.sleep(60)
		continue



# -*- coding: utf-8 -*-

# Copyright (c) 2018, Altiria TIC SL
# All rights reserved.
# El uso de este código de ejemplo es solamente para mostrar el uso de la pasarela de envío de SMS de Altiria
# Para un uso personalizado del código, es necesario consultar la API de especificaciones técnicas, donde también podrás encontrar
# más ejemplos de programación en otros lenguajes de programación y otros protocolos (http, REST, web services)
# https://www.altiria.com/api-envio-sms/

'''

def altiriaSms(destinations, message, senderId, debug):
	if debug:
		print('Enter altiriaSms: '+destinations+', message: '+message+', senderId: '+senderId)
		try:
			#Se crea la lista de parámetros a enviar en la petición POST
			#XX, YY y ZZ se corresponden con los valores de identificación del usuario en el sistema.
			payload = [
			    ('cmd', 'sendsms'),
			    ('domainId', 'XX'),
			    ('login', 'YY'),
			    ('passwd', 'ZZ'),
                            #No es posible utilizar el remitente en América pero sí en España y Europa
                            ('senderId', senderId),
			    ('msg', message)
			]

			#add destinations
			for destination in destinations.split(","):
			    payload.append(('dest', destination))

			#Se fija la codificacion de caracteres de la peticion POST
			contentType = {'Content-Type':'application/x-www-form-urlencoded;charset=utf-8'} 
		
			#Se fija la URL sobre la que enviar la petición POST
			url = 'http://www.altiria.net/api/http'

			#Se envía la petición y se recupera la respuesta
			r = requests.post(url, data=payload, headers=contentType, timeout=(5, 60))
			    #Se fija el tiempo máximo de espera para conectar con el servidor (5 segundos)
			    #Se fija el tiempo máximo de espera de la respuesta del servidor (60 segundos)
			    #timeout(timeout_connect, timeout_read)

			if debug:
				if str(r.status_code) != '200': #Error en la respuesta del servidor
					print('ERROR GENERAL: '+str(r.status_code))
				else: #Se procesa la respuesta 
					print('Código de estado HTTP: '+str(r.status_code))
				if (r.text).find("ERROR errNum:"):
					print('Error de Altiria: '+r.text)
				else:
					print('Cuerpo de la respuesta: \n'+r.text )	

			return r.text

		except  requests.ConnectTimeout:
			print("Tiempo de conexión agotado")
		
		except  requests.ReadTimeout:
			print("Tiempo de respuesta agotado")

		except Exception as ex:
			print("Error interno: "+str(ex))
		
print('The function altiriaSms returns: \n'+altiriaSms('346xxxxxxxx,346yyyyyyyy','Mesaje de prueba', '', True))
#No es posible utilizar el remitente en América pero sí en España y Europa
#Utilizar esta llamada solo si se cuenta con un remitente autorizado por Altiria
#print 'The function altiriaSms returns: \n'+altiriaSms('346xxxxxxxx,346yyyyyyyy','Mesaje de prueba', 'remitente', True)

'''