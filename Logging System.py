import csv
import os
from re import DEBUG
import pandas as pd
import random



if os.path.exists("Log_in_data.csv")== False:#this ensure that if a csv doesn't exist it will make one so that the program still works.

    f=open("Log_in_data.csv","x")# creates the file if it does not exist
    f.close()


    f=open("Log_in_data.csv","a",newline="")
    headers=("user_id","username","password")#this creates the headers for the new file
    writer=csv.writer(f)
    writer.writerow(headers)

    f.close()

def UniqueId():#this function generates a unique id for the user
  print("In the function")
  AttemptId = ""
  ContainsId = True #Contains id is a boolean that is set to true in the first place so that it runs through the creation of a new id
  
  while ContainsId == True:
    #Creating the id
    for i in range(0,16):
      AttemptId += str(random.randint(0,9))
    
    f = open("Log_in_data.csv", "r")
    
    reader = csv.reader(f)
    
    if  AttemptId in f:
      ContainsId = True
      
    else:
      ContainsId = False
      ID = AttemptId
      f.close()
      
      print(ID)
      
      return ID

  
YorN=input("Do you have a account? yes/no")
if YorN =="yes":#if the user has an account it will ask for the username and password then read the csv and check if the username and password are in the csv. If the username and password are in the csv it will print "you are logged in" and if not it will print you are not logged in.
  user_inp=input("please enter your username")
  pass_inp=input("please enter your password")
  with open("Log_in_data.csv","r") as f:
    reader=csv.reader(f)
    for row in reader:
      if row[1]==user_inp and row[2]==pass_inp:
        print("you are logged in")
        break
      else:
        print("you are not logged in")
        break
elif YorN=="no":#If the user does not have an account it will ask for the username and password then append it to the csv and print you are logged in.
  user_inp=input("please enter your username")
  pass_inp=input("please enter your password")
  with open("Log_in_data.csv","a",newline="") as f:
    
    writer=csv.writer(f)

    ID = UniqueId()

    print(ID)
    
    writer.writerow({ID,user_inp,pass_inp})

    print("your account has been created")
    YorN=input("would you like to log in? yes/no")
    if YorN=="yes":
      
      
    
    
    
    
    
  
