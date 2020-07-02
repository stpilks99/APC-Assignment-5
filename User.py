import sqlite3
import sys

database = sqlite3.connect('CURSE.db')
c = database.cursor()

class User:

    # constructor
    def __init__(self, firstName, lastName, ID):
        self.firstName = firstName
        self.lastName = lastName
        self.ID = ID

    # author: Naomi Torre
    # login function
    def login(self):
        user = input("Are you a Student, Admin or Instructor? ")
        if user == 'Student' or user == 'Admin' or user == 'Instructor':
            username = input("Enter username: ")
            upassword = input("Enter password: ") 
        
            #Checking credentials
            c.execute("""SELECT Email from '""" + user + """' WHERE '""" + user + """'.Email = '""" + username + """';""")
            qr1 = c.fetchall()
        
            for i in qr1:
                result1 = i[0]
        
            c.execute("""SELECT Password from '""" + user + """' WHERE Password = '""" + upassword + """' AND Email = '""" + username + """';""")
            qr2= c.fetchall()
        
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

    # author: Naomi Torre
    # search all courses function
    def searchAllCourses(self):
        print("\nHere are all the courses: \n")
        c.execute("""SELECT * from Course """)
        qr = c.fetchall()
        for i in qr:
            print(i)

    # author: Naomi Torre
    # search courses with parameters
    def searchCoursesByParam(self):
        print("Here are the parameters to search by: \n1 to search by semester \n2 to search title \n3 to search by CRN \n4 to search by department \n5 to search by instructor \n6 to search by time \n7 to search by days \n8 to search by credits")
        choice = input("Enter number that corresponds to parameter of choice: ")
        
        if choice == '1':
            term = input("\nEnter the semester in which you would like to search courses for: ")
            yr = input("\nEnter the year of the semester: ")
            c.execute("""SELECT * from Course WHERE Semester = '""" + term + """' AND Year = '""" + yr + """';""")
            qr = c.fetchall()
            
            print("\nHere are all the courses in " + term + " " + yr + ":\n")
            for i in qr:
                print(i)
        
        elif choice == '2':
            title = input("Enter title to search by: ")
            c.execute("""SELECT * from Course WHERE Title = '""" + title + """';""")
            qr = c.fetchall()
            
            print("\nHere are all the courses titled " + title + ":\n")
            for i in qr:
                print(i)
        
        elif choice == '3':
            crn = input("Enter CRN to search by: ")
            c.execute("""SELECT * from Course WHERE CRN = '""" + crn + """';""")
            qr = c.fetchall()
            
            print("\nHere are all the courses with " + crn + " as a CRN:\n")
            for i in qr:
                print(i)
            
        elif choice == '4':
            department = input("Enter department to search by: ")
            c.execute("""SELECT * from Course WHERE Department = '""" + department + """';""")
            qr = c.fetchall()
            
            print("\nHere are all the courses in the department " + department + ":\n")
            for i in qr:
                print(i)
            
        elif choice == '5':
            instructor = input("Enter instructor to search by: ")
            c.execute("""SELECT * from Course WHERE Instructor = '""" + instructor + """';""")
            qr = c.fetchall()
            
            print("\nHere are all the courses taught by " + instructor + ":\n")
            for i in qr:
                print(i)
            
        elif choice == '6':
            time = input("Enter time to search by: ")
            c.execute("""SELECT * from Course WHERE Times = '""" + time + """';""")
            qr = c.fetchall()
            
            print("\nHere are all the courses taught at  " + time + ":\n")
            for i in qr:
                print(i)
            
        elif choice == '7':
            days = input("Enter days to search by: ")
            c.execute("""SELECT * from Course WHERE DaysOfWeek = '""" + days + """';""")
            qr = c.fetchall()
            
            print("\nHere are all the courses taught on " + days + ":\n")
            for i in qr:
                print(i)
        
        elif choice == '8':
            creds = input("Enter number of credits to search by: ")
            c.execute("""SELECT * from Course WHERE Credits = '""" + creds + """';""")
            qr = c.fetchall()
            
            print("\nHere are all the courses with " + creds + " credits: \n")
            for i in qr:
                print(i)
        else: 
            print('invalid choice! \n Please try again.')
            searchCoursesByParam()

    # author: Naomi Torre
    # search courses function           
    def searchCourses(self):
        num = input("\nEnter 1 to search all courses or 2 to search with parameters: ")
        if num == '1':
            searchAllCourses()
        elif num == '2':
            searchCoursesByParam()
        else:
            print("invalid choice! \n Please try again.")
            searchCourses()

    # author: Naomi Torre
    # logout function    
    def logout(self):
        print(" \nYou have successfully logged out. \nFor security reasons, exit your web browser.")
        sys.exit()

class Student(User):

    # constructor
    def __init__(self, firstName, lastName, ID):
        super().__init__(firstName, lastName, ID)
        print('Student {} {} [{}] created'.format(self.firstName, self.lastName, self.ID))

    # add courses to student schedule
    # author: Chandler Berry
    def addCourse(self, studentID, studentEmail):

        # prompt user to enter CRN
        getCRN = input('enter CRN of course you want to add: ')

        # get ID of student adding the course to their schedule
        getStudentID = 'SELECT Student.ID FROM Student WHERE Student.Email = \'' + studentEmail + '\''
        c.execute(getStudentID)
        studentResult = list(c.fetchall())

        # get initial student schedule
        getSched = 'SELECT Student.Schedule FROM Student WHERE Student.ID = ' + studentID
        c.execute(getSched)
        schedule = list(c.fetchall())

        # get initial course roster
        getRoster = 'SELECT Course.Roster FROM Course WHERE Course.CRN = ' + getCRN
        c.execute(getRoster)
        roster = list(c.fetchall())

        # add student ID to course roster in Course table
        newRoster = ''
        for row in roster:
            if row[0] == None:
                for value in studentResult:
                    newRoster = value[0]
            elif row[0] != None:
                for value in studentResult:
                    newRoster = str(row[0]) + '-' + str(value[0])
        updateRoster = 'UPDATE Course SET Roster = \'' + newRoster + '\' WHERE Course.CRN = ' + getCRN
        c.execute(updateRoster)

        # add course to student schedule
        newSchedule = ''
        for row in schedule:
            if row[0] == None:
                for value in studentResult:
                    newSchedule = getCRN
            elif row[0] != None:
                for value in studentResult:
                    newSchedule = str(row[0]) + '-' + getCRN
        updateSched = 'UPDATE Student SET Schedule = \'' + newSchedule + '\' WHERE Student.ID = ' + studentID
        c.execute(updateSched)
        
        # commit changes to db
        database.commit()

    # remove courses from student schedule
    # author: Chandler Berry
    def rmCourse(self, studentID, studentEmail):

        # prompt user to enter CRN
        getCRN = input('enter CRN of course you want to remove: ')

        # get ID of student removing the course from their schedule
        getStudentID = 'SELECT Student.ID FROM Student WHERE Student.Email = \'' + studentEmail + '\''
        c.execute(getStudentID)
        studentResult = list(c.fetchall())

        # get initial student schedule
        getSched = 'SELECT Student.Schedule FROM Student WHERE Student.ID = ' + studentID
        c.execute(getSched)
        schedule = list(c.fetchall())

        # get initial course roster
        getRoster = 'SELECT Course.Roster FROM Course WHERE Course.CRN = ' + getCRN
        c.execute(getRoster)
        roster = list(c.fetchall())

        # remove student ID from course roster in Course table
        newRoster = ''
        for row in roster:
            if row[0] == None:
                print('you aren\'t registered in this course')
            elif row[0] != None:
                findID = ''
                for value in studentResult:
                    findID = row[0]
                    if str(value[0]) in findID:
                        newRoster = findID
                        if '-' in newRoster:
                            rosterList = newRoster.split('-')
                            rosterList.remove(str(value[0]))
                            s = '-'
                            newRoster = s.join(rosterList)
                        else:
                            newRoster = ''
                    else:
                        print('you aren\'t registered in this course')
        updateRoster = 'UPDATE Course SET Roster = \'' + newRoster + '\' WHERE Course.CRN = ' + getCRN
        c.execute(updateRoster)

        # remove course from student schedule
        newSched = ''
        for row in schedule:
            if row[0] == None:
                print('you aren\'t registered in this course')
            elif row[0] != None:
                findCRN = ''
                for value in schedule:
                    findCRN = row[0]
                    if str(value[0]) in findCRN:
                        newSched = findCRN
                        if '-' in newRoster:
                            schedList = newSched.split('-')
                            schedList.remove(str(value[0]))
                            s = '-'
                            newSched = s.join(schedList)
                        else:
                            newSched = ''
                    else:
                        print('you aren\'t registered in this course')
        updateSched = 'UPDATE Student SET Schedule = \'' + newSched + '\' WHERE Student.ID = ' + studentID
        c.execute(updateSched)
        
        # commit changes to db
        database.commit()

    # author: Sterling
    # student menu function
    def studentMenu(self):
        choice=""

        while 1:
            choice = input("Welcome to the CURSE registration system.\n1. Add a course\n2. Drop a course\n3. Search courses\n4. View/print schedule\n5. Check conflicts\n6. Logout\nEnter choice : ")
            if choice == '1':
                print("Add a course to your schedule.")
                addCourse()
            elif choice == '2':
                print("Drop a course from your schedule.")
                rmCourse()
            elif choice == '3':
                print("Searching courses.")
                searchCourses()
            elif choice == '4':
                print("Please select a semester and year : ")
                #printSchedule()
            elif choice == '5':
                print("Checking schedule for conflicts.")
                #checkConflict()
            elif choice == '6':
                print("Logging out...")
                logout()

# class Instructor derived from User
class Instructor(User):

    # constructor
    def __init__(self, firstName, lastName, ID):
        super().__init__(firstName, lastName, ID)
        print('Instructor {} {} [{}] created'.format(self.firstName, self.lastName, self.ID))

    def printRoster(self):
        getCRN = input('enter CRN of course to view roster: ')
        getRoster = 'SELECT Course.Roster FROM Course WHERE Course.CRN = ' + getCRN
        c.execute(getRoster)
        rosterResult = list(c.fetchall())

        rosterString = ''
        for row in rosterResult:
            rosterString = row[0]
        
        rosterList = []
        if '-' in rosterString:
            rosterList = rosterString.split('-')
        else:
            rosterList.append(rosterString)
        
        studentNames = []
        for studentID in rosterList:
            getStudentNames = 'SELECT Student.FirstName, Student.LastName, Student.Major, Student.GradYear FROM Student WHERE Student.ID = ' + studentID
            c.execute(getStudentNames)
            studentItems = c.fetchall()
            studentNames.append(studentItems)

        for eachStudent in studentNames:
            studentInfo = str(eachStudent[0][0]) + ' ' + str(eachStudent[0][1]) + ' - ' + str(eachStudent[0][2]) + ' - Class of ' + str(eachStudent[0][3])
            print(studentInfo) 

    # author: Sterling
    # instructor menu function
    def instructorMenu(self):
        choice=""

        while 1:
            choice = input("Welcome to the CURSE registration system.\n1. Search courses\n2. View/print schedule\n3. Print roster\n4. Logout\nEnter choice : ")
            if choice == '1': 
                print("Searching courses.")
                searchCourses()
            elif choice == '2':
                print("Please select a semester and year : ")
            elif choice == '3': 
                print("Please select a course to print roster : ")
                printRoster()
            elif choice == '4':
                print("Logging out...")
                logout()

# class admin derived from user
class admin(User):  
    # constructor
    def __init__(self, firstName, lastName, ID):
        super().__init__(firstName, lastName, ID)
        print('Admin {} {} [{}] created'.format(self.firstName, self.lastName, self.ID)) 

    # author: Sterling
    # add courses to system function
    def addCourseSys(self):
        print("Adding a course to the system.")
        title = input("Title : ")
        CRN = input("CRN : ")
        
        #checking if the CRN already exists
        c.execute("""SELECT * FROM COURSE WHERE CRN = """ + CRN + """;""")
        # fetchone() returns a 0 if nothing was found
        query_result = c.fetchone()

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
            c.execute("""INSERT INTO COURSE VALUES('""" + title + """', """ + CRN + """, '""" + dept + """', '""" + fName + """', '""" + lName + """', '""" + time + """', '""" + day + """', '""" + semester + """', """ + year + """, """ + cred + """);""")
            c.execute("""SELECT * FROM COURSE WHERE CRN = """ + CRN + """;""")
            query_result = c.fetchone()
            for i in query_result:
                print(i)
            print("Success! Course added to system.")

        # commit changes to db
        database.commit()    
        

    # author: Sterling
    # remove courses from system
    def removeCourseSys(self):
        print("Removing a course from the system.")
        removeCRN = input("Enter CRN of course to remove : ")
        c.execute("""SELECT * FROM COURSE WHERE CRN = """ + removeCRN + """;""")
        query_result = c.fetchone()
        if (query_result is None):
            print("Error: CRN entered does not match a course in the database.")
        else:
            for i in query_result:
                print(i)
            choice = input("Are you sure you want to remove this? y/n : ")
            if (choice == 'y'):
                c.execute("""DELETE FROM COURSE WHERE CRN = """ + removeCRN + """;""")
                print("Success.")
            else:
                print("Canceled. No changes have been made.")

        # commit changes to db
        database.commit()    

    # author: Sterling
    # admin menu function
    def adminMenu(self):
        choice = ""

        while 1:
            choice = input("Welcome to the CURSE registration system.\n1. Add a course to system\n2. Remove a course from system\n3. Search courses\n4. View/print schedule\n5. Print roster\n6. Link/unlink user from course\n7. Add user\n8. Logout\nEnter choice : ")
            if choice == '1':
                addCourseSys()
            elif choice == '2':
                removeCourseSys()
            elif choice == '3':
                print("Searching courses.")
                searchCourses()
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
                logout()

c.close()
database.close()