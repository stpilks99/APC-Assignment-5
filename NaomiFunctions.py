"""
APC: Assignment 5 

"""

import sqlite3
import sys

# database file connection 
database = sqlite3.connect("CURSE.db") 

cursor = database.cursor()

def login():
    user = input("Are you a Student, Admin or Instructor? ")
    if user == 'Student' or user == 'Admin' or user == 'Instructor':
        username = input("Enter username: ")
        upassword = input("Enter password: ") 
    
        #Checking credentials
        cursor.execute("""SELECT Email from '""" + user + """' WHERE '""" + user + """'.Email = '""" + username + """';""")
        qr1 = cursor.fetchall()
    
        for i in qr1:
            result1 = i[0]
    
        cursor.execute("""SELECT Password from '""" + user + """' WHERE Password = '""" + upassword + """' AND Email = '""" + username + """';""")
        qr2= cursor.fetchall()
    
        for i in qr2:
            result2 = i[0]
        try:
            if username == result1 and upassword == result2 :
                print("\nLogin successful!")
                #if user == Student:
                    #studentMenu()
                #elif user == Instructor:
                    #instructorMenu()
                #elif user == Admin:
                    #adminMenu()
        except UnboundLocalError as error:
            print("\ninvalid credentials.")
            again = input("Would you like to try again? \nEnter 1 to go back to login \nEnter 2 to exit\n")
            if again == '1':
                login()
            elif again == '2': 
                sys.exit()
            
    else: 
        print('\nPlease enter a correct user type.')
        login()

def searchAllCourses():
    print("\nHere are all the courses: \n")
    cursor.execute("""SELECT * from Course """)
    qr = cursor.fetchall()
    for i in qr:
    	print(i)

def searchCoursesByParam():
    print("Here are the parameters to search by: \n1 to search by semester \n2 to search title \n3 to search by CRN \n4 to search by department \n5 to search by instructor \n6 to search by time \n7 to search by days \n8 to search by credits")
    choice = input("Enter number that corresponds to parameter of choice: ")
    
    if choice == '1':
        term = input("\nEnter the semester in which you would like to search courses for: ")
        yr = input("\nEnter the year of the semester: ")
        cursor.execute("""SELECT * from Course WHERE Semester = '""" + term + """' AND Year = '""" + yr + """';""")
        qr = cursor.fetchall()
        
        print("\nHere are all the courses in " + term + " " + yr + ":\n")
        for i in qr:
        	print(i)
    
    elif choice == '2':
        title = input("Enter title to search by: ")
        cursor.execute("""SELECT * from Course WHERE Title = '""" + title + """';""")
        qr = cursor.fetchall()
        
        print("\nHere are all the courses titled " + title + ":\n")
        for i in qr:
        	print(i)
    
    elif choice == '3':
        crn = input("Enter CRN to search by: ")
        cursor.execute("""SELECT * from Course WHERE CRN = '""" + crn + """';""")
        qr = cursor.fetchall()
        
        print("\nHere are all the courses with " + crn + " as a CRN:\n")
        for i in qr:
        	print(i)
        
    elif choice == '4':
        department = input("Enter department to search by: ")
        cursor.execute("""SELECT * from Course WHERE Department = '""" + department + """';""")
        qr = cursor.fetchall()
        
        print("\nHere are all the courses in the department " + department + ":\n")
        for i in qr:
        	print(i)
        
    elif choice == '5':
        instructor = input("Enter instructor to search by: ")
        cursor.execute("""SELECT * from Course WHERE Instructor = '""" + instructor + """';""")
        qr = cursor.fetchall()
        
        print("\nHere are all the courses taught by " + instructor + ":\n")
        for i in qr:
        	print(i)
        
    elif choice == '6':
        time = input("Enter time to search by: ")
        cursor.execute("""SELECT * from Course WHERE Times = '""" + time + """';""")
        qr = cursor.fetchall()
        
        print("\nHere are all the courses taught at  " + time + ":\n")
        for i in qr:
        	print(i)
        
    elif choice == '7':
        days = input("Enter days to search by: ")
        cursor.execute("""SELECT * from Course WHERE DaysOfWeek = '""" + days + """';""")
        qr = cursor.fetchall()
        
        print("\nHere are all the courses taught on " + days + ":\n")
        for i in qr:
        	print(i)
    
    elif choice == '8':
        creds = input("Enter number of credits to search by: ")
        cursor.execute("""SELECT * from Course WHERE Credits = '""" + creds + """';""")
        qr = cursor.fetchall()
        
        print("\nHere are all the courses with " + creds + " credits: \n")
        for i in qr:
        	print(i)
    else: 
        print('invalid choice! \n Please try again.')
        searchCoursesByParam()
            
def searchCourses():
    num = input("\nEnter 1 to search all courses or 2 to search with parameters: ")
    if num == '1':
        searchAllCourses()
    elif num == '2':
        searchCoursesByParam()
    else:
        print("invalid choice! \n Please try again.")
        searchCourses()
    
def logout():
    print(" \nYou have successfully logged out. \nFor security reasons, exit your web browser.")
    sys.exit()
 
login()
searchCourses()
logout()
