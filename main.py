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
        

        print("\n\nPlease wait....\nChecking details....\nRegistration successfull\n\nThanks for choosing Medicare!!...\n")

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
                appointment_phone = int(input("\nEnter your phone number  :  "))
                
        except ValueError:
                print('\nInvalid choice !!, restart the programme...\n')
                exit()
        appointment_gender = input('\nEnter gender (M/F)  :  ')
        appointment_bg = input("\nEnter your Blood group  :  ")
        appointment_adress = input("\nEnter your address  :  ")
        
        cursor.execute('SELECT DISTINCT Department FROM doctors_info ORDER BY Department')
        appointment_booking_fetchall = cursor.fetchall()
        
        if 1 <= appointment_div <= 12:
            print('\nChecking Credentials...\nChecking available Doctors...\nLooking for Vacant appointments...\nPlease wait...\n')
        
            appointment_dep = appointment_booking_fetchall[appointment_div - 1][0]
        
            try:

                cursor.execute("SELECT * FROM patients_info")
                cursor.execute("""INSERT INTO patients_info (ID, Name, Age, Gender, B_goup, Address, Phone) VALUES (%s, %s, %s, %s, %s, %s, %s)""",(f"PT9U{len(cursor.fetchall()) + 1}", appointment_name , appointment_age ,appointment_gender , appointment_bg , appointment_adress, "+91 " + str(appointment_phone)))
                connection.commit()

                cursor.execute("""SELECT Names FROM doctors_info WHERE Department = %s""",(appointment_dep,))
        
                doctors_list = cursor.fetchall()
                cursor.execute('SELECT * FROM appointments')
                a = cursor.fetchall()

                cursor.execute("SELECT ID FROM patients_info")
                b = cursor.fetchall()

                cursor.execute("""SELECT consulting_fee FROM departments WHERE Department_name = %s""" , (appointment_dep,))
                fee = cursor.fetchall()[0]
        
                cursor.execute("""INSERT INTO appointments(ID,P_Name,Doctor,Division,date,patient_ID,Consulting_fee) VALUES (%s,%s,%s,%s,%s,%s,%s)""",(f'AP9U{len(a) + 1}' , appointment_name , rnd.choice(doctors_list)[0] , appointment_dep , dt.date.today() , b[len(b) - 1][0]) , fee)
        
                connection.commit()

                cursor.execute('SELECT Doctor From appointments')

                doctor = cursor.fetchall()[len(cursor.fetchall()) - 1][0]
                
                cursor.execute('SELECT patient_ID FROM appointments')
                c = cursor.fetchall()
                print(f'\nAppointment Booked successfully !! , Details are shown below :\n\n')
        
                print(pd.DataFrame({
                    "ID\n(Remember it)" : [f"AP9U{len(c)}"],
                    "Patient" : [appointment_name],
                    "Age" : [appointment_age],
                    "Division" : [appointment_dep],
                    "Doctor appointed" : [doctor],
                    "Consulting\nFee(INR)" : [fee],
                    "Date of\nAppointment" : [dt.date.today()],
                    "Patient ID\n(Remember it)" : [c[len(c) - 1][0]]
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
                            "Date of\nappointment" : [appointment_details_fetch[0][4]],
                            "Patient\nID" : [appointment_details_fetch[0][5]],
                            "Consulting\nfee(INR)" : [appointment_details_fetch[0][6]]
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
        hospital_service_choice = int(input('\n1) Departments\n2) Laboratories\n3) Ambulance\n\nChoose as per your requirement  :  '))
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

    elif hospital_service_choice == 2:
            
        try:
            choose_test = int(input("\nChoose medical Division of your test :-\n\n1) CBC / Complete Blood Count\n2) Blood Sugar\n3) Lipid Profile\n4) Liver Function Test\n5) Kidney Function Test\n6) Thyroid Profile\n7) Urine Test\n8) X-Ray\n9) CT Scan\n10) MRI\n\nChoose as per your requirement  :  "))
        except ValueError:
            print("\nInvalid input !!, Retart the programme\n\nThanks for visiting MEDICARE...\n")
            exit()

        try:
            cursor.execute("SELECT Test FROM laboratory_tests")

            cursor.execute("""SELECT * FROM laboratory_tests WHERE Test=%s""",(cursor.fetchall()[choose_test - 1][0],))

            tests_fetchall = cursor.fetchall()
            print("\nDetails of this test are :- \n")

            print(pd.DataFrame({
                "ID" : [tests_fetchall[0][0]],
                "Test\nname" : [tests_fetchall[0][1]],
                "Description" : [tests_fetchall[0][2]],
                "Charges" : ["INR " + str(tests_fetchall[0][3])],
                "Department" : [tests_fetchall[0][4]]
            }).to_markdown(index=False))

            try:
                ask_test = int(input("\nWould you like to book this test for tommorrow?\n\n1) Yes\n2) No\n\nChoose as per requirement  :  "))
            except ValueError:
                print("\nInvalid input !!, Retart the programme\n\nThanks for visiting MEDICARE...\n")
                exit()

            if ask_test == 1:
                print("\nBook your Lab Test now just in minutes...\n")
                test_cont_name = input("\nEnter Patient's name  :  ")
                try:
                    test_cont_age = int(input("\nEnter age  :  "))
                    test_cont_phone = int(input("\nEnter phone numnber (+91)  :  "))
                except ValueError:
                    print("\nInvalid input !!, Retart the programme\n\nThanks for visiting MEDICARE...\n")
                    exit()
                test_cont_gender = input("\nEnter Patient's gender (M/F)  :  ")
                test_cont_bg = input("\nEnter Patient's blood group  :  ")
                test_cont_add = input("\nEnter address  :  ")

                cursor.execute("SELECT * FROM lab_test_bookings")
                length = len(cursor.fetchall())

                cursor.execute("SELECT * FROM patients_info")
                cursor.execute("""INSERT INTO patients_info (ID, Name, Age, Gender, B_goup, Address, Phone) VALUES (%s, %s, %s, %s, %s, %s, %s)""",(f"PT9U{len(cursor.fetchall()) + 1}", test_cont_name , test_cont_age , test_cont_gender , test_cont_bg ,test_cont_add, "+91 " + str(test_cont_phone)))
                connection.commit()

                cursor.execute("SELECT ID FROM patients_info")
                p_id_for_test = cursor.fetchall()

                cursor.execute("""SELECT Charges FROM laboratory_tests WHERE Test = %s""" , (tests_fetchall[0][4],))
                charges = cursor.fetchall()[0][0]

                cursor.execute("""INSERT INTO lab_test_bookings (ID , Name , Age , Gender , Phone_NO , Department , Date , patient_ID , Test_charges) VALUES (%s,%s,%s,%s,%s,%s,%s)""",(f"TA9U{length + 1}" , test_cont_name , test_cont_age , test_cont_gender , "+91 " + str(test_cont_phone) , tests_fetchall[0][4] , dt.date.today() + dt.timedelta(days=1) , p_id_for_test[len(p_id_for_test) - 1][0] , charges))

                connection.commit()

                cursor.execute("SELECT ID FROM lab_test_bookings")

                print(f"\nChecking details...\nChecking avaialibility...\nPlease wait...\n\nYour Lab test Booking ID is {cursor.fetchall()[len(cursor.fetchall()) - 1][0]}\n\nDigital portal of MEDICARE doesn't allows cancellation of lab test booking , so please visit nearest MEDICARE branch to cancel your lab test booking\n\nThanks for choosisng MEDICARE...\n")

            else:
                print("\nThanks for visiting MEDICARE...\n")
                exit()
        except mysql.connector.Error as err:
            print(f"\nOOPS !! , looks like some error occured From our server side : {err}, please try again by restarting the programme\n\nThanks for choosing MEDICARE...\n")
            exit()
        finally:
            cursor.close()
            connection.close()
    elif hospital_service_choice == 3:
        print("\n===================================================================================")
        print("                             Ambulance Portal                                        ")
        print("===================================================================================\n")

        try:
            ambulance_service_choice = int(input("\n1) View  Ambulance\n2) Request an ambulance\n\nChoose as per your requirement  :  "))
        except ValueError:
            print("\nInavlid input ! , TRy again by restarting the programme\n\nThanks to visit MEDICARE...\n")
            exit()
        if ambulance_service_choice == 1:
            try:
                cursor.execute("SELECT * FROM ambulance_record ORDER BY ID")
                ambulance_record = cursor.fetchall()

                print("\nHere are the details of all ambulances of MEDICARE :-\n\n")
                print(pd.DataFrame({
                    "ID" : [i[0] for i in ambulance_record],
                    "Status" : [i[1] for i in ambulance_record]
                }).to_markdown(index=False))
                print('\nThanks for Choosing MEDICARE...\n')
            except mysql.connector.Error as err:
                print(f"\nOOPS !! , looks like some error occured From our server side : {err}, please try again by restarting the programme\n\nThanks for choosing MEDICARE...\n")
            finally:
                cursor.close()
                connection.close()

        elif ambulance_service_choice == 2:
            get_amb_name = input("\nEnter your name  :  ")

            for i in range(len(get_amb_name)):
                if get_amb_name[i] not in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ":
                    print("\nInvalid name enrty !, Try agian by restarting the programme\n\nThanks for choosing MEDICARE...\n")
                    exit()
                else:
                    if i == len(get_amb_name) - 1:
                        try:

                            cursor.execute("SELECT ID FROM ambulance_record WHERE status='Available'")
                            ambulances = cursor.fetchall()
                            ambulance_given = rnd.choice(ambulances) # Giving ambulance to user randomly from available ambulances

                            cursor.execute("select * from ambulance_bookings")
                            cursor.execute("""INSERT INTO ambulance_bookings (ID,Name,Ambulance,Fee) VALUES (%s,%s,%s,%s)""",(f"AB9U{len(cursor.fetchall()) + 1}" , get_amb_name , ambulance_given[0] , 250.0)) # updating the booking table
                            connection.commit()
                            cursor.execute("""UPDATE ambulance_record SET status='On Duty' WHERE ID=%s""",(ambulance_given[0],))
                            connection.commit()
                            print(f"\nChecking availablity of ambulance...\n\nFetching database...\n\nSuccessfully booked a ambualnce \nAmbulance ID is {ambulance_given[0]}\nThanks for chhoosing MEDICARE...\n")
                        except mysql.connector.Error as err:
                            print(f"\nOOPS !! , looks like some error occured From our server side : {err}, please try again by restarting the programme\n\nThanks for choosing MEDICARE...\n")
                            exit()
                        finally:
                            cursor.close()
                            connection.close()

                    else:
                        continue
        else:
            print("\nPrint Invalid choice !, Try again  by restarting the programme\n\nThanks for choosing MEDICARE...\n")

            # Welcome Dev chauhan.....