# Edgar Gonzalez
# 2030467
# Importamos librerias necesarias

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Preparamos los datos necesarios para el correo

remitente = 'soloparayt184@gmail.com' #Aqui va tu correo
destinatario= 'edgar.gonzalezprd@uanl.edu.mx' # Aqui va pues el destinatario
asunto = 'PRACTICA 12' # El asunto del correo

# Se le da escructura al mensaje
msg=MIMEMultipart()
msg['Subject'] = asunto
msg['From'] = remitente
msg['To'] = destinatario

with open('miemail.html', 'r') as archivo:
    html = archivo.read()

# Se adjunta el contenido HTML
msg.attach(MIMEText(html, 'html'))

#Se realiza server con el servidor SMTP
server =smtplib.SMTP('smtp.gmail.com', 587)

#Se pone los datos para realizar la server con 
#nuestro correo

server.starttls()
server.login('soloparayt184@gmail.com', 'asrc irdo emxt uczn') # es tu correo y contraseña de app

#Se envia el correo
server.sendmail(remitente,destinatario,msg.as_string())

#se desconecta la server
server.quit()
