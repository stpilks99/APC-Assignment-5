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

    def searchAllCourses(self):
        print("\nHere are all the courses: \n")
        c.execute("""SELECT * from Course """)
        qr = c.fetchall()
        for i in qr:
            print(i)

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
                
    def searchCourses(self):
        num = input("\nEnter 1 to search all courses or 2 to search with parameters: ")
        if num == '1':
            searchAllCourses()
        elif num == '2':
            searchCoursesByParam()
        else:
            print("invalid choice! \n Please try again.")
            searchCourses()
        
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

c.close()
database.close()