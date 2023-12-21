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


def create_acc():#this function creates a new account by asking the user to input a username and password and addding it to the csv file.
  user_inp=input("please enter your username")

  pass_inp=input("please enter your password")

  with open("Log_in_data.csv","a",newline="") as f:

    writer=csv.writer(f)

    UniqueId()
    writer.writerow([ID,user_inp,pass_inp])

    print("your account has been created")
    f.close()

def login_in():#this function asks the user to input their username and password and checks if it is in the csv file. If the inputs match they are logged in.
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

def UniqueId():#this function generates a unique id for the user
    AttemptId = ""
    for i in range(07):
        AttemptId += str(random.randint(0,9))
        global ID
        ID=AttemptId
