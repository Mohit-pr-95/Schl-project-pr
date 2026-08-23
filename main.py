# --------- School project ----------
# --------- Author : Mohit singh & Dev chauhan -------------
# --------- Date : 22/08/2026 ------------------------------


import numpy as np
import pandas as pd
import datetime as dt
import random as rd

print("------------------- Welcome to the digital portal of Medicare Hospital -------------------\n\n")

try:
    choose_service = int(input("1) Patient portal\n2) Doctor's portal\n3) Appointments\n4) More services\n5) Billing\n6) Emergency information\n7) About the hospital\n8) Exit\n\nChoose as per your requirement  :  "))
except ValueError:
    print("Invalid choice!!, please enter appropriate service number...")
    exit()

if choose_service == 1:
    try:
        patient_service_choice = int(input("1) Register patient\n2) View patient detail\n3) Search patients\n\nChoose as per your requirement  :  "))
    except ValueError:
        print("Invalid choice!!, please enter appropriate service number...")
        exit()

    if patient_service_choice == 1:
        patient_name = input("Enter name of patient  :  ")
        try:
            patient_age = int(input("Enter age  :  "))
            patient_phone = int(input("Enter phone number  :  "))
        except ValueError:
            print("Invalid entry !!, Try again by restarting the programme")
            exit()

        patient_gender = input("Enter patient's gender (M/F)  :  ")
        patient_adress = input("Enter address  :  ")
        patient_bg = input("Enter Blood group  :  ")

        with open("C:\\Users\\Mohit Singh\\OneDrive\\Desktop\\my_work\\Schl-project-pr\\patients.txt","r") as r:
            data = r.readlines()

            sum = 0
            for i in data:
                if i.startswith("-"):
                    sum += 1
            
            with open("C:\\Users\\Mohit Singh\\OneDrive\\Desktop\\my_work\\Schl-project-pr\\patients.txt","a") as f:

                f.write(f"---------------------------------------- p {sum+1} ---------------------------------\n\nPatient Name : {patient_name}\nPatient age : {patient_age}\nPatient gender : {patient_gender}\nPatient Blood group : {patient_bg}\nPatient contact : +91 {patient_phone}\nPatient address : {patient_adress}\n\n")

        print("\n\nPlease wait....\nChecking details....\nRegistration successfull\n\nThanks for choosing Medicare!!...")

