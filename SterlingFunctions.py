# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 18:38:12 2020

@author: pilkingtons
"""

# Sterling: 
# Add/remove courses from the system (admin)
# A menu to implement the use-cases

import sqlite3

# database file connection 
database = sqlite3.connect("CURSE.db") 
cursor = database.cursor() 

# so it doesn't give an error about the table already existing
cursor.execute("""DROP TABLE IF EXISTS COURSE;""")

# inserting course data 
sql_command = """CREATE TABLE COURSE (
TITLE          TEXT    PRIMARY KEY NOT NULL,
CRN            INT     NOT NULL,
DEPT           CHAR(4) NOT NULL,
NAME           TEXT    NOT NULL,
SURNAME        TEXT    NOT NULL,
TIME           TEXT    NOT NULL,
DAYS_OF_WEEK   TEXT    NOT NULL,
SEMESTER       TEXT    NOT NULL,
YEAR           TEXT    NOT NULL,
CREDITS        TEXT    NOT NULL,
FOREIGN KEY (NAME) REFERENCES INSTRUCTOR(NAME),
FOREIGN KEY (SURNAME) REFERENCES INSTRUCTOR(SURNAME),
FOREIGN KEY (DEPT) REFERENCES INSTRUCTOR(DEPT))
;"""

# execute the statement 
cursor.execute(sql_command) 

# Course List
cursor.execute("""INSERT INTO COURSE VALUES('Intro to Advertising', 12345, 'HUSS', 'Nelson', 'Mandela', '1:00 PM - 2:50 PM', 'TR', 'Summer', '2020', 4);""")
cursor.execute("""INSERT INTO COURSE VALUES('Drawing II', 54321, 'BSAS', 'Galileo', 'Galilei', '8:00 AM - 9:20', 'WF', 'Summer', '2020', 4)""") 
cursor.execute("""INSERT INTO COURSE VALUES('Computer Networks for Engineers', 11934, 'BSCO', 'Alan', 'Turing', '8:00 AM - 9:20 AM', 'TR', 'Summer', '2020', 4);""") 
cursor.execute("""INSERT INTO COURSE VALUES('Operating Systems Research', 21443, 'BCOS', 'Katie', 'Bouman', '9:30 AM - 10:50 AM', 'TR', 'Summer', 2020, 4);""") 
cursor.execute("""INSERT INTO COURSE VALUES('Thermodynamics', 42804, 'BSME', 'Daniel', 'Bournoulli', '10:00 AM - 11:50 AM', 'MW', 'Summer', 2020, 4);""") 

# printing all classes
print("All courses : ")
cursor.execute("""SELECT * FROM COURSE""")
query_result = cursor.fetchall()
# printing each row of the query
for i in query_result:
	print(i)
  


def addCourseSys():
    print("Adding a course to the system.")
    title = input("Title : ")
    CRN = input("CRN : ")
    
    #checking if the CRN already exists
    cursor.execute("""SELECT * FROM COURSE WHERE CRN = """ + CRN + """;""")
    # fetchone() returns a 0 if nothing was found
    query_result = cursor.fetchone()

    #result that returned 
    if (query_result is not None):
        print("Error : CRN already exists.")
        for i in query_result:
            print(i)
            
    else:
        dept = input("Department : ")
        fName = input("Instructor first name : ")
        lName = input("Instructor last name : ")
        time = input("Time slot : ")
        day = input("Days (MTWRF) : ")
        semester = input("Semester (Fall, Spring, Summer) : ")
        year = input("Year : ")
        cred = input("# of credits : ")
        # inserting new info into database
        cursor.execute("""INSERT INTO COURSE VALUES('""" + title + """', """ + CRN + """, '""" + dept + """', '""" + fName + """', '""" + lName + """', '""" + time + """', '""" + day + """', '""" + semester + """', """ + year + """, """ + cred + """);""")
        cursor.execute("""SELECT * FROM COURSE WHERE CRN = """ + CRN + """;""")
        query_result = cursor.fetchone()
        for i in query_result:
            print(i)
        print("Success! Course added to system.")
        

def removeCourseSys():
    print("Removing a course from the system.")
    removeCRN = input("Enter CRN of course to remove : ")
    cursor.execute("""SELECT * FROM COURSE WHERE CRN = """ + removeCRN + """;""")
    query_result = cursor.fetchone()
    if (query_result is None):
        print("Error: CRN entered does not match a course in the database.")
    else:
        for i in query_result:
            print(i)
        choice = input("Are you sure you want to remove this? y/n : ")
        if (choice == 'y'):
            cursor.execute("""DELETE FROM COURSE WHERE CRN = """ + removeCRN + """;""")
            print("Success.")
        else:
            print("Canceled. No changes have been made.")
        

def studentMenu():
    choice=""
    loggedIn=1
    while loggedIn==1:
        choice = input("Welcome to the CURSE registration system.\n1. Add a course\n2. Drop a course\n3. Search courses\n4. View/print schedule\n5. Check conflicts\n6. Logout\nEnter choice : ")
        if choice == '1':
            print("Add a course to your schedule.")
            #addCourse()
        elif choice == '2':
            print("Drop a course from your schedule.")
            #dropCourse()
        elif choice == '3':
            print("Searching courses.")
            #searchCourses()
        elif choice == '4':
            print("Please select a semester and year : ")
            #printSchedule()
        elif choice == '5':
            print("Checking schedule for conflicts.")
            #checkConflict()
        elif choice == '6':
            print("Logging out...")
            loggedIn=0
            #logout()
        
def instructorMenu():
    choice=""
    loggedIn=1
    while loggedIn==1:
        choice = input("Welcome to the CURSE registration system.\n1. Search courses\n2. View/print schedule\n3. Print roster\n4. Logout\nEnter choice : ")
        if choice == '1': 
            print("Searching courses.")
        elif choice == '2':
            print("Please select a semester and year : ")
        elif choice == '3': 
            print("Please select a course to print roster : ")
        elif choice == '4':
            print("Logging out...")
            loggedIn=0
        
def adminMenu():
    choice = ""
    loggedIn=1
    while loggedIn==1:
        choice = input("Welcome to the CURSE registration system.\n1. Add a course to system\n2. Remove a course from system\n3. Search courses\n4. View/print schedule\n5. Print roster\n6. Link/unlink user from course\n7. Add user\n8. Logout\nEnter choice : ")
        if choice == '1':
            addCourseSys()
        elif choice == '2':
            removeCourseSys()
        elif choice == '3':
            print("Searching courses.")
        elif choice == '4':
            print("Enter WID# of user to view their schedule : ")
        elif choice == '5': 
            print("Enter CRN to print roster : ")
        elif choice == '6':
            print("Link/unlink student or instructor to course.")
        #linkUnlink
        elif choice == '7':
            print("Add student or instructor?")
        elif choice == '8':
            print("Logging out...")
            loggedIn=0
        
#addCourseSys()        
#removeCourseSys()
        
def main():
    adminMenu()
    studentMenu()
    instructorMenu()

if __name__ == '__main__':
    main()
    
# todo: 
# make sure admin can't type in wrong data types for inputs

# fix "Operational Error: database is locked."

#if (CRN=="[("+CRN+",)]")

#[]

#[(12345,)]

#if 


