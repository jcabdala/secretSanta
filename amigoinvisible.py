#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from time import sleep
import copy
import smtplib
import random

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

from config import chicos, grandes, usermail, passwmail, subjectmail

# send email from python
# this creates a text email and sends it to an address of your choosing directly from python
def mailsend (toaddress, fromaddress, subject, message):
    # you need to know your correct smtp server for this to work, mine is in the function below
    # The actual mail send
    msg = MIMEMultipart()
    msg['From'] = fromaddress
    msg['To'] = toaddress
    msg['Subject'] = subject
    msg.attach(MIMEText(message))
    server = smtplib.SMTP("smtp.live.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(usermail, passwmail)
    server.sendmail(fromaddress, toaddress, msg.as_string())
    server.quit()
    """
    the below calls the function - you should change the address settings for your purposes, 
    and you can change the subject and message details as well to send the message information you want to send
    """


#amigo= id, grande, chico, mail
grandes_aux=copy.deepcopy(grandes.keys())

for id in grandes:
    # print id,":"
    amigoGrande = id
    while id == amigoGrande:
        amigoGrande = random.choice(grandes_aux)
    grandes_aux.remove(amigoGrande)
    # print amigoGrande
    amigoChico = random.choice(chicos)
    # print amigoChico
    chicos.remove(amigoChico)
    # print grandes
    info = "Mail oficial del amigo Invisible 2016, tus amigos son: " + amigoGrande + " y " + amigoChico
    print "Sending to", grandes[id]
    mailsend (grandes[id], usermail,subjectmail, info)
    sleep(2)
