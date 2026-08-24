# --------- School project ----------
# --------- Author : Mohit singh & Dev chauhan -------------
# --------- Date : 22/08/2026 ------------------------------

import os
from dotenv import load_dotenv
import mysql.connector # Importing SQL for table database managament through python script
import pandas as pd
import datetime as dt

load_dotenv()

# connecting to local MySQL server
connection = mysql.connector.connect(
    host = os.getenv("Database_host"),
    user = os.getenv("Database_user"),
    password = os.getenv("Database_pass"),
    database = os.getenv("Database_name")
)

cursor = connection.cursor()

print("\n===================================================================================")
print("                             Medicare Hospital Welcomes you                          ")
print("===================================================================================\n")

try:
    choose_service = int(input("1) Patient portal\n2) Doctor's portal\n3) Appointments\n4) More services\n5) Billing\n6) Emergency information\n7) About the hospital\n8) Exit\n\nChoose as per your requirement  :  "))
except ValueError:
    print("Invalid choice!!, please enter appropriate service number...")
    exit()

if choose_service == 1:
    print("\n===================================================================================")
    print("                             Patient's Portal                                        ")
    print("===================================================================================\n")
    try:
        patient_service_choice = int(input("1) Register patient\n2) View patient detail\n3) Search patients\n\nChoose as per your requirement  :  "))
    except ValueError:
        print("Invalid choice!!, please enter appropriate service number...")
        exit()

    if patient_service_choice == 1:
        patient_name = input("\nEnter name of patient  :  ")
        try:
            patient_age = int(input("Enter age  :  "))
            patient_phone = int(input("Enter phone number  :  "))
        except ValueError:
            print("Invalid entry !!, Try again by restarting the programme")
            exit()

        patient_gender = input("Enter patient's gender (M/F)  :  ")
        patient_adress = input("Enter address  :  ")
        patient_bg = input("Enter Blood group  :  ")

        try:
            cursor.execute("""INSERT INTO Patient_name (Name, Age, Gender, Blood_group, Phone, Address) VALUES (%s, %s, %s, %s, %s, %s)""",(patient_name,patient_age,patient_gender,patient_bg,"+91" + str(patient_phone),patient_adress))

            connection.commit() # Telling MySQL to save the above changes in database

        except mysql.connector.Error as err:
            print(f"Error : {err}")
            print("Registration failed...!!")
            exit()
        finally:
            cursor.close() # Closing cursor object
            connection.close() # Closing server connection from script 
        

        print("\n\nPlease wait....\nChecking details....\nRegistration successfull\n\nThanks for choosing Medicare!!...")

elif choose_service == 2:
    print("\n===================================================================================")
    print("                             Doctor's Portal                                         ")
    print("===================================================================================\n")

    