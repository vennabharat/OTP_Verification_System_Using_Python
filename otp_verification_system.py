# -*- coding: utf-8 -*-
"""OTP_Verification_System.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rr99Bh0HWrhpEa8b4LsKTymqml8QtE-n

**function for OTP generation**

---
"""

def otp_generator():  #function for generating otp
  otp = ""  #variable for keeping track of the generated numbers
  import random as rand # importing random library
  for i in range(6):  # for loop to generate 6 numbers
    otp = otp+str(rand.randint(0,9))  #converting random int to string and concatinating to otp variable
  return otp  # returning otp

"""**Function for sending email to the user**"""

def send_otp(np):  #function for sending email to the user
  sender = 'v.bharath39@gmail.com'  #sender email
  password = 'ldcv khca wztc qczz'  #app specific password

  import smtplib  #importing smtp library
  server = smtplib.SMTP('smtp.gmail.com', 587)  #creating object used for gmail domain
  server.starttls() #starting server with tls protocol
  server.login(sender, password)  #logging in to the sender

  subject = "OTP Verification"  #email subject
  body = f"Your OTP is {np}" #email body
  message = f"subject:{subject}\n\n{body}"  #encoding subject and body
  receiver = input('Enter your email address to login:') #input for obtaining user email id

  import re
  pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
  if re.match(pattern, receiver):
    server.sendmail(sender, receiver, message)  #sending email using server
    return np
  else:
    print('Invalid email address')
    return None

"""**Function to prompt the user to enter the otp**"""

def enter_otp():  #function to prompt the user to enter the otp
  u_otp = input('Enter OTP that you received over mail:')  #input for obtaining user otp
  return u_otp  #returning user otp

"""**converting otp to hashcode and verification**"""

import bcrypt  #importing bcrypt library

def hash_otp(otp) -> bytes:  #function to convert otp to hashcode and mailing the code to the user
  !pip install bcrypt  #installing bcrypt library
  hashed = bcrypt.hashpw(otp.encode('utf-8'), bcrypt.gensalt())  #converting otp to hashcode
  #send_otp()  #calling send_otp
  return hashed  #returning hashcode

def verify_otp(enter_otp, hash_otp):
  return bcrypt.checkpw(enter_otp().encode('utf-8'), hash_otp)  #checking for user entered otp

#print(hash_otp(send_otp(otp_generator())))

"""testing the code"""

hashed = hash_otp(send_otp(otp_generator()))  #storing encoded password for verification
for i in range(3):  #3 repetitions for entering otp
  if verify_otp(enter_otp, hashed):
    print('OTP Verified')
    break
  else:
    print('OTP Incorrect\nRetry')