#!/usr/bin/python3

from python_terraform import *
import sys
import os
import argparse
import json
import boto3
#import ansible_runner

import pandas as pd

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders



sender='devanandareddy.raptadu@ovaledge.com'
sender_pass='Dev@0213'
msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = "devanandareddy.raptadu@ovaledge.com;mahesh.ramichetty@ovaledge.com"
msg['Subject'] = "SAAS application "

dns = "BCU.ovaledge.cloud"
mail_cust = dns[:dns.index("ovaledge.cloud")-1]
mail_license="UJH+uAs3MMb7YCIjPWestF26P/FFPoJekYdqBeyCuO5KieunNMiFswEvgwgY62pgf6YmRpBTJqKHia+qsQ84iYsGteVVBALqjh/XnbuFvsuvmRAzKXs+5tu7HfloFnOVIRHdA3Ob+O5wK4WkoX4KdmKurE/4RuCvubLZN4Z5DdM="
##body = """Hi """+mail_cust+""" Team,\nGreetings of the day!\nCongratulations on your first step toward a Progressive Data Governance Journey!\n
##Please follow the below instructions to start the journey :\n
##Step 1: Click on """+base_url+"""login\n
##Step 2: Plug in your License Key in the License Page displayedon clicking the above URL :\n"""+License+"""\nStep 3: Make a note of the username and the password that is generated\n
##Step 4: Log in to the application with the above credentials\n
##Step 5: Change the password (recommended)\n
##Step 6: Begin your journey"""

html_in = open(r"D:\deva documents\SAAS\2.final-saas-files\python\ovaledge_testmail.html", "rt")
html_data = html_in.read()
html_data = html_data.replace('SAAScustomer', mail_cust)
html_data = html_data.replace('SAASlicense', mail_license)
html_in.close()

html_out=open(r"D:\deva documents\SAAS\2.final-saas-files\python\ovaledge_mainmail.html", "wt")
html_out.write(html_data)
html_out.close()

report_file = open(r'D:\deva documents\SAAS\2.final-saas-files\python\ovaledge_mainmail.html')
body = report_file.read()
##body1 = """Hi please follow below instructions"""

##msg.attach(MIMEText(body1, 'plain'))

msg.attach(MIMEText(body, 'html'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(sender, sender_pass)
server.send_message(msg)
server.quit()
print("mail sent")
