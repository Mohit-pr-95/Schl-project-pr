# --------- School project ----------
# --------- Author : Mohit singh & Dev chauhan -------------
# --------- Mohit singh (Python code writer) & dev chauhan (Database manager) ------------
# --------- Date : 22/08/2026 ------------------------------

import os
from dotenv import load_dotenv
import mysql.connector # Importing SQL for table database managament through python script
import pandas as pd
import datetime as dt
import random as rnd

load_dotenv()

# connecting to local MySQL server
try:

    connection = mysql.connector.connect(
    host = os.getenv("Database_host"),
    user = os.getenv("Database_user"),
    password = os.getenv("Database_pass"),
    database = os.getenv("Database_name")
    )
except mysql.connector.Error as error:
    print(f'Some error arised in connecting with SQL server : {error}\nRestart the programme...')
    exit()

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

        if  get_id.startswith("PT9U"):

            try:
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
            except mysql.connector.Error as err:
                print(f"\nOOPS!!, Looks like some error occured : {err}\nTry again by restarting the programme, \nThanks for choosing MEDICARE...\n")
                exit()

            finally:
                cursor.close()
                connection.close()
        else:
            print("\nInvalid ID !!, Try again by restarting the programme, \nThanks for choosing MEDICARE...\n")
            exit()
        
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

elif choose_service == 3:
    print("\n===================================================================================")
    print("                             Appointments                                            ")
    print("===================================================================================\n")

    try:
        appointment_services = int(input('\n1) Book appointments\n2) View appointment\n3) Cancel appointment\n\nChoose as per your requirement  :  '))
    except ValueError:
        print('Inavlid input !!, enter a valid choice , Restart the programme...\nThanks to visit MEDICARE...\n')
        exit()

    if appointment_services == 1:
        appointment_name = input("\nEnter Patient's name  :  ")
        try:
                appointment_age = int(input("\nEnter age  :  "))
                appointment_div = int(input('\n1) Cardiology\n2) Dermatology\n3) Endocrinology\n4) Gynecology\n5) Neurology\n6) Oncology\n7) Ophthalmology\n8) Orthopedics\n9) Pediatrics\n10) Psychiatry\n11) Radiology\n12) Urology\n\nChoose Your category  :  '))
        except ValueError:
                print('Invalid choice !!, restart the programme...')
                exit()
        appointment_gender = input('\nEnter gender (M/F)  :  ')
        
        cursor.execute('SELECT DISTINCT Department FROM doctors_info ORDER BY Department')
        appointment_booking_fetchall = cursor.fetchall()
        
        if 1 <= appointment_div <= 12:
            print('\nChecking Credentials...\nChecking available Doctors...\nLooking for Vacant appointments...\nPlease wait...\n')
        
            appointment_dep = appointment_booking_fetchall[appointment_div - 1][0]
        
            try:
                cursor.execute("""SELECT Names FROM doctors_info WHERE Department = %s""",(appointment_dep,))
        
                doctors_list = cursor.fetchall()
                cursor.execute('SELECT * FROM appointments')
        
                cursor.execute("""INSERT INTO appointments(ID,P_Name,Doctor,Division,date) VALUES (%s,%s,%s,%s,%s)""",(f'AP9U{len(cursor.fetchall()) + 1}' , appointment_name , rnd.choice(doctors_list)[0] , appointment_dep , dt.date.today()))
        
                connection.commit()

                cursor.execute('SELECT Doctor From appointments')

                doctor = cursor.fetchall()[len(cursor.fetchall()) - 1][0]
        
                cursor.execute('SELECT * FROM appointments')
        
                print(f'\nAppointment Booked successfully !! , Details are shown below :\n\n')
        
                print(pd.DataFrame({
                    "ID\n(Remember it)" : [f"AP9U{len(cursor.fetchall())}"],
                    "Patient" : [appointment_name],
                    "Age" : [appointment_age],
                    "Division" : [appointment_dep],
                    "Doctor appointed" : [doctor],
                    "Date of\nAppointment" : [dt.date.today()]
                    }).to_markdown(index=False))
        
                print("\nThanks for choosing MEDICARE...\n")
        
            except mysql.connector.Error as err:
                print(f'OOPS!!, Looks like some error arised : {err}\nRestart the programme\nThanks for choosing MEDICARE...\n')
                exit()
        
            finally:
                cursor.close()
                connection.close()
        else:
            print('Invalid choice!!, Retstart the programme...\nThanks for choosing MEDICARE...\n')
            exit()
        
    elif appointment_services == 2: # Creating 'View appointment' Feature
        get_appointment_id = input("\nEnter your Appointment ID  :  ")
        if get_appointment_id.startswith("AP9U"):

            try:
                cursor.execute("SELECT ID FROM appointments")
                x = cursor.fetchall()

                for i in range(len(x)):
                    if x[i][0] == get_appointment_id:
                        cursor.execute("""SELECT * FROM appointments WHERE ID=%s""",(get_appointment_id,)) # Dev chauhan
                        appointment_details_fetch = cursor.fetchall() # getting all appointment details

                        print('\nFetching database...\nFetching your ID...\nPlease wait...\n\nYour appointment details are : \n')
                        print(pd.DataFrame({
                            "ID" : [appointment_details_fetch[0][0]],
                            "Name of\nPatient" : [appointment_details_fetch[0][1]],
                            "Doctor\nAppointed" : [appointment_details_fetch[0][2]],
                            "Division" : [appointment_details_fetch[0][3]],
                            "Date of\nappointment" : [appointment_details_fetch[0][4]]
                        }).to_markdown(index=False))
                        print('\nThanks for choosing MEDICARE...\n')
                    else:
                        if i == len(x) - 1:
                            print(f"\nNo user with id {get_appointment_id} Found in database, Check your entered ID and try again!!, \nThanks for choosing MEDICARE...\n")
                            exit()

            except mysql.connector.Error as err:
                print(f"\nOOPS!!, Looks like some error occured : {err}\nTry again by restarting the programme, \nThanks for choosing MEDICARE...\n")
                exit()
            finally:
                cursor.close()
                connection.close()

        else:
            print("\nInvalid ID !!, Try again by restarting the programme, \nThanks for choosing MEDICARE...\n")

    elif appointment_services == 3: # Creating 'Cancel appointment' Feature
            cancel_appointment_id = input("\nEnter your Appointment ID which is to be cancelled :  ")

            if cancel_appointment_id.startswith("AP9U"):
                try:
                    cursor.execute("SELECT ID FROM appointments")
                    y = cursor.fetchall()
    
                    for i in range(len(y)):
                        if y[i][0] == cancel_appointment_id:
                            cursor.execute("""DELETE FROM appointments WHERE ID=%s""",(cancel_appointment_id,)) # Dev chauhan

                            connection.commit()
                            print('\nFetching database...\nFetching your ID...\nPlease wait...\n\nYour appointment is cancelled successfully : \n')
                            print('\nThanks for choosing MEDICARE...\n')
                            
                        else:
                            if i == len(y) - 1:
                                print(f"\nNo user with id {cancel_appointment_id} Found in database, Check your entered ID and try again!!, \nThanks for choosing MEDICARE...\n")
                                exit()
    
                except mysql.connector.Error as err:
                    print(f"\nOOPS!!, Looks like some error occured : {err}\nTry again by restarting the programme, \nThanks for choosing MEDICARE...\n")
                    exit()
                finally:
                    cursor.close()
                    connection.close()
    
            else:
                print("\nInvalid ID !!, Try again by restarting the programme, \nThanks for choosing MEDICARE...\n")
    else:
        print('\nInvalid choice , try again by restarting the programme!!, \nThanks for choosing MEDICARE...\n')
    
elif choose_service == 4:
    print("\n===================================================================================")
    print("                             Hospital services                                       ")
    print("===================================================================================\n")

    try:
        hospital_service_choice = int(input('\n1) Departments\n2) Laboratories\n3) Ambulance\n4) Pharmacy\n\nChoose as per your requirement  :  '))
    except ValueError:
        print("Inavlid Input , Retstart the programme\nThanks for choosing MEDIACRE...\n")
        exit()

    if hospital_service_choice == 1:
        try:
            department_service_choice = int(input('\n1) View all Departments\n2) Get details of a particular department\n\nChoose as per your requirement  :  '))
        except ValueError:
            print('Invalid input , retstart the programme !!\nThanks for choosing MEDICARE...\n')
            exit()

        if department_service_choice == 1:
            try:
                cursor.execute('SELECT DISTINCT Department FROM doctors_info ORDER BY Department')

                print('\nList of all departments :-\n')

                print(pd.DataFrame({
                    "S.no." : [i for i in range(1,13)],
                    "Departments" : [i[0] for i in cursor.fetchall()]
                }).to_markdown(index=False))

                print('\nThanks for choosing MEDICARE...\n')
            except mysql.connector.Error as err:
                print(f"\nOOps ! looks like some error occured in SQL server : {err}\nRestart the programme\n\nThanks for choosing MEDICARE...\n")
                exit()
            finally:
                cursor.close()
                connection.close()

        elif department_service_choice == 2:
            try:
                department_detail_choice = int(input('\n1) Cardiology\n2) Dermatology\n3) Endocrinology\n4) Gynecology\n5) Neurology\n6) Oncology\n7) Ophthalmology\n8) Orthopedics\n9) Pediatrics\n10) Psychiatry\n11) Radiology\n12) Urology\n\nChoose department  :  '))
            except ValueError:
                print('\nInvalid choice !!, restart the programme...\n')
                exit()
            try:
                cursor.execute('SELECT Department_Name FROM departments ORDER BY Department_Name')

                cursor.execute("""SELECT * FROM departments WHERE Department_Name=%s""",(cursor.fetchall()[department_detail_choice - 1][0],))

                department_details = cursor.fetchall()

                cursor.execute("""SELECT * FROM doctors_info WHERE Department=%s""",(department_details[0][1],))
                print(f"\nDetails of the department \"{department_details[0][1]}\" are here :- \n")
                print(pd.DataFrame({
                    "ID" : [department_details[0][0]],
                    "Department\nname" : [department_details[0][1]],
                    "Description\nof department" : [department_details[0][2]],
                    "Number of\nDoctors" : [len(cursor.fetchall())]
                }).to_markdown(index=False))

                print("\nDoctors available in this department are :- \n")

                cursor.execute("""SELECT * FROM doctors_info WHERE Department=%s""",(department_details[0][1],))
                z = cursor.fetchall()
                print(pd.DataFrame({
                    "ID" : [i[0] for i in z],
                    "Name\nof Doctor" : [i[1] for i in z],
                    "Experience\n(in years)" : [i[3] for i in z]
                }).to_markdown(index=False))
                print('\nThanks for choosing MEDICARE...\n')
            except mysql.connector.Error as err:
                print("OOPS !!, looks like some error occured , Retstart the programme \nThanks for choosing MEDICARE...\n")
                exit()

            finally:
                cursor.close()
                connection.close()
                
        else:
            print("Invalid choice !, Restart the programme\n\nThanks for choosing MEDICARE...\n")