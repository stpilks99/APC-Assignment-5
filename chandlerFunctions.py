import sqlite3

database = sqlite3.connect('CURSE.db')
c = database.cursor()

# add courses to student schedule
# author: Chandler Berry
def addCourse(studentID, studentEmail):

    # prompt user to enter CRN
    getCRN = input('enter CRN of course you want to add: ')

    # get ID of student adding the course to their schedule
    getStudentID = 'SELECT Student.ID FROM Student WHERE Student.Email = \'' + studentEmail + '\''
    c.execute(getStudentID)
    studentResult = list(c.fetchall())

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

    # get initial student schedule
    getSched = 'SELECT Student.Schedule FROM Student WHERE Student.ID = ' + studentID
    c.execute(getSched)
    schedule = list(c.fetchall())

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


addCourse('10001', 'newtoni')

# # remove courses from student schedule
# # author: Chandler Berry
# def rmCourse():
#     getCRN = input('enter CRN of course you want to remove')

# # print course roster for instructor
# # author: Chandler Berry
# def printRoster():
#     getCRN = input('enter CRN of course to view roster')


c.close()
database.close()