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
        patient_service_choice = int(input("1) Register patient\n2) View patient detail\n\nChoose as per your requirement  :  "))
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
            cursor.execute("SELECT * FROM patients_info")
            
            cursor.execute("""INSERT INTO patients_info (ID, Name, Age, Gender, B_goup, Address, Phone) VALUES (%s, %s, %s, %s, %s, %s, %s)""",(f"PT9U{len(cursor.fetchall()) + 1}", patient_name,patient_age,patient_gender,patient_bg,patient_adress, "+91 " + str(patient_phone)))

            connection.commit() # Telling MySQL to save the above changes in database

        except mysql.connector.Error as err:
            print(f"Error : {err}")
            print("Registration failed...!!")
            exit()
        finally:
            cursor.close() # Closing cursor object
            connection.close() # Closing server connection from script 
        

        print("\n\nPlease wait....\nChecking details....\nRegistration successfull\n\nThanks for choosing Medicare!!...")

    elif patient_service_choice == 2:

        get_id = input("\nEnter the patient's ID(PT9U..)  :  ")
        cursor.execute('SELECT * FROM patients_info')
        p_data = cursor.fetchall()
        for i in range(len(p_data)):
            for j in range(len(p_data[i])):
                if p_data[i][j] == get_id:
                    pInfo = pd.DataFrame({
                        "ID" : [p_data[i][j]],
                        "Name" : [p_data[i][j+1]],
                        "Age" : [p_data[i][j+2]],
                        "Gender" : [p_data[i][j+3]],
                        "B_group" : [p_data[i][j+4]],
                        "Address" : [p_data[i][j+5]],
                        "Phone" : [p_data[i][j+6]]
                    })

                    print("\nInfo of patient is shown below :- \n")
                    print(pInfo.to_markdown(index=False))
                    print('\nThanks to visit MEDICARE Hospital...\n')

                    break
                else:
                    if j == len(p_data[i])-1 and i == len(p_data)-1:
                        print(f'\nFetching database....\nVerifying ID....\n\nSorry!!, No patient found having ID {get_id}\n\nThanks for visiting MEDICARE Hospital digital portal!...\n')

        cursor.close()
        connection.close()
        
    else:
        print('Invalid choice !!, Enter a valid option number...\n')

elif choose_service == 2:
    print("\n===================================================================================")
    print("                             Doctor's Portal                                         ")
    print("===================================================================================\n")

    try:
        doctor_service_choice = int(input('\n1) View doctors\n2) Search doctors by department\n\nChoose as per your requirement  :  '))
    except ValueError:
        print('Invalid choice!!, please enter appropriate service number...')
        exit()

    if doctor_service_choice == 1:
        cursor.execute("SELECT * FROM doctors_info")
        d_data = cursor.fetchall()

        doctor_ids = [i[0] for i in d_data]
        names = [i[1] for i in d_data]
        specialization = [i[2] for i in d_data]
        experience = [i[3] for i in d_data]

        table = pd.DataFrame({
            "ID" : doctor_ids,
            "Names" : names,
            "Specialization" : specialization,
            "Experience\n(Years)" : experience
        })

        print('\nHere is complete list of doctors of "MEDICARE Hospital"\n')
        print(table.to_markdown(index=False))
        print('\nThanks to visit MEDICARE Hospital digital portal..\n')

    elif doctor_service_choice == 2:

        try:
            get_department = int(input('\n1) Cardiology\n2) Dermatology\n3) Endocrinology\n4) Gynecology\n5) Neurology\n6) Oncology\n7) Ophthalmology\n8) Orthopedics\n9) Pediatrics\n10) Psychiatry\n11) Radiology\n12) Urology\n\nChoose department  :  '))
        except ValueError:
            print('Invalid choice !!, restart the programme...')
            exit()

        if get_department in range(1,13):

            cursor.execute("SELECT DISTINCT Department FROM doctors_info ORDER BY Department")
            departments = cursor.fetchall()

            cursor.execute("""SELECT * FROM doctors_info WHERE Department = %s""",(departments[get_department-1][0],))

            doc_data = cursor.fetchall()

            doc_ids = [i[0] for i in doc_data]
            doc_names = [i[1] for i in doc_data]
            doc_specialization = [i[2] for i in doc_data]
            doc_experience = [i[3] for i in doc_data]

            doc_table = pd.DataFrame({
            "ID" : doc_ids,
            "Names" : doc_names,
            "Specialization" : doc_specialization,
            "Experience\n(Years)" : doc_experience
            })

            print(f'\nFetching database...\nChecking departement...\nPlase wait...\n\nlist of all doctors in {departments[get_department-1][0]} :-\n')

            print(doc_table.to_markdown(index=False))

            print("\nThanks for choosing MEDICARE...\n")
        else:
            print('Invalid departement choice, Restart the programme...\n')
            exit()

    else:
        print('Invalid choice !!, Restart the programme...\n')
        exit()