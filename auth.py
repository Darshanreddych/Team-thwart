import os
import random
from twilio.rest import Client 
import datetime

users = {'darshanreddych@gmail.com':'Darshan@123' ,  'preethuppoojary@gmail.com':'Preethu@123', 'darshanappu149@gmail.com':'Darshan@123','mohammadarshad14310@gmail.com':'Arshad@123','pereira.reshma.lp@gmail.com':'Reshma@123'}

account_sid = 'AC58785c7b66aec4f949ec34e19be86f8b'
auth_token = '3e2132ab8a05c2f03ea1afcf56d8d523'
client = Client(account_sid,auth_token)
flag=0
while True:
	OTP=""
	for i in range(6):
		otp=random.getrandbits(3)
		OTP+=str(otp)
	
	msg=" This is your otp " + str(OTP)
	user= input("enter user email id---->  ")
	if user in users:
		passw=input("enter password----> ")
		if passw==users[user]:
			message = client.messages.create(
					body = msg,
					from_='+12055435065',
					to= input("enter mobile number to send otp ")
					)
			while True:		
				otp1= input("enter otp sent--->  ")
				if otp1==OTP:
					print("@@@@@@Login succesful@@@@@@ ")
					
					flag=1	
					break
				else:
					print("*****enter valid otp******")
					
			if flag==1:
				break
			
					
		else:
			print("*******entered wrong passkey********** ")
	else:
		print("*******enter valid email id**********")
