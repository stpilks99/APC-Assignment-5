import sqlite3

database = sqlite3.connect('CURSE.db')
c = database.cursor()

c.execute('DROP TABLE IF EXISTS Student')
c.execute('DROP TABLE IF EXISTS Instructor')
c.execute('DROP TABLE IF EXISTS Admin')
c.execute('DROP TABLE IF EXISTS Course')

createStudentTable = """
CREATE TABLE Student (  
    ID 			INT 	    PRIMARY KEY NOT NULL,
    FirstName	TEXT	    NOT NULL,
    LastName	TEXT 	    NOT NULL,
    GradYear	INT 	    NOT NULL,
    Major		CHAR(4)     NOT NULL,
    Email		TEXT	    NOT NULL,
    Username    TEXT        NOT NULL,
    Password    TEXT        NOT NULL,
    Schedule    BLOB
);
"""
c.execute(createStudentTable)

createInstructorTable = """
CREATE TABLE Instructor (
    ID          INT         PRIMARY KEY NOT NULL,
    FirstName   TEXT        NOT NULL,
    LastName    TEXT        NOT NULL,
    Title       TEXT        NOT NULL,
    Department  CHAR(4)     NOT NULL,
    Email       TEXT        NOT NULL,
    Username    TEXT        NOT NULL,
    Password    TEXT        NOT NULL,
    Schedule    BLOB
);
"""
c.execute(createInstructorTable)

createAdminTable = """
CREATE TABLE Admin (
    ID          INT         PRIMARY KEY NOT NULL,
    FirstName   TEXT        NOT NULL,
    LastName    TEXT        NOT NULL,
    Email       TEXT        NOT NULL,
    Username    TEXT        NOT NULL,
    Password    TEXT        NOT NULL
);
"""
c.execute(createAdminTable)

createCourseTable = """
CREATE TABLE Course (
    CRN         INT         PRIMARY KEY NOT NULL,
    Title       TEXT        NOT NULL,
    Department  CHAR(4)     NOT NULL,
    Instructor  TEXT        NOT NULL,
    DaysOfWeek  TEXT        NOT NULL,
    Semester    TEXT        NOT NULL,
    Year        TEXT        NOT NULL,
    Credits     TEXT        NOT NULL,
    Roster      BLOB
);
"""
c.execute(createCourseTable)

c.close()
database.close()