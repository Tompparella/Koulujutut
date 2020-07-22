# Db Inserter.
# Tommi Kunnari 0543382
# 22.7.2020

# This program makes it easy to insert new data into the given university.db
# database. It also generates the phone number and email address for student and teacher tables
# to avoid unnecessary typing. If this was database intended for real use that would naturally be taken out.
# The program has to be stored in the same path as the .db file.


import sqlite3
import sys
from random import randrange
from sqlite3 import Error

file = 'university.db'

def create_conn():
    # Connects to database file
    conn = None
    try:
        conn = sqlite3.connect(file)
        print('Connected.\nSQLite3 version:', sqlite3.version)
        return conn
    except Error as e:
        print('Connection failed. Error:', e)
        sys.exit()
        

def main():
    conn = create_conn()
    while True:
        # Looping menu
        print("""1. Add student\n2. Add Course\n3. Add teacher\n4. Add classroom
5. Add enrollment\n6. Add degree\n7. Add course_rooms\n8. Add course_teacher\n0. End program""")
        choice = input("Choose what to do: ")
        if choice == "1":
            add_student(conn)
        elif choice == "2":
            add_course(conn)
        elif choice == "3":
            add_teacher(conn)
        elif choice == "4":
            add_classroom(conn)
        elif choice == "5":
            add_enrollment(conn)
        elif choice == "6":
            add_degree(conn)
        elif choice == "7":
            add_course_rooms(conn)
        elif choice == "8":
            add_course_teacher(conn)
        elif choice == "0":
            end_program(conn)
        else:
            print("Bad input.\n")
    
# Functions for adding different entries

def add_student(conn):
    s_id = input("Student id: ")
    f_name = input("First name: ")
    l_name = input("Last name: ")
    e_date = input("Enroll date: ")
    undergrad = input("Undergraduate? (1/0): ")
    exchange = input("Exchange? (1/0): ")
    phone = randrange(358400000000, 358409999999)
    email = f_name + "." + l_name + "@student.lut.fi"
    try:
        conn.execute("insert into student values (%s, '%s', '%s', '%s', %s, %s, '%s', '%s')" % (s_id, f_name, l_name, e_date, undergrad, exchange, phone, email))
        print("\nAdded entry succesfully!\n")
    except Error as e:
        print("Error: ", e)

def add_course(conn):
    c_id = input("Course id: ")
    c_name = input("Course name: ")
    c_credits = input("Credits: ")
    try:
        conn.execute("insert into course values (%s, '%s', %s)" % (c_id, c_name, c_credits))
        conn.commit()
        print("\nAdded entry succesfully!\n")
    except Error as e:
        print("Error: ", e)

def add_teacher(conn):
    t_id = input("Teacher id: ")
    f_name = input("First name: ")
    l_name = input("Last name: ")
    h_date = input("Hire date: ")
    phone = randrange(358400000000, 358409999999)
    email = f_name + "." + l_name + "@lut.fi"
    try:
        conn.execute("insert into teacher values (%s, '%s', '%s', '%s', '%s', '%s')" % (t_id, f_name, l_name, h_date, phone, email))
        print("\nAdded entry succesfully!\n")
    except Error as e:
        print("Error: ", e)

def add_classroom(conn):
    r_id = input("Room id: ")
    r_name = input("Room name: ")
    seats = input("Seats: ")
    is_usable = input("Usable? (1/0): ")
    try:
        conn.execute("insert into classroom values (%s, '%s', %s, %s)" % (r_id, r_name, seats, is_usable))
        print("\nAdded entry succesfully!\n")
    except Error as e:
        print("Error: ", e)

def add_enrollment(conn):
    s_id = input("Student id: ")
    c_id = input("Course id: ")
    grade = input("Grade (leave empty if unfinished): ")
    date = input("Start- and end dates (leave open if ongoing): ")
    try:
        conn.execute("insert into enrollments values (%s, %s, '%s', '%s')" % (s_id, c_id, grade, date))
        print("\nAdded entry succesfully!\n")
    except Error as e:
        print("Error: ", e)

def add_degree(conn):
    t_id = input("Teacher id: ")
    degree = input("Degree name: ")
    try:
        conn.execute("insert into degrees values (%s, '%s')" % (t_id, degree))
        print("\nAdded entry succesfully!\n")
    except Error as e:
        print("Error: ", e)

def add_course_rooms(conn):
    c_id = input("Course id: ")
    r_id = input("Room id: ")
    usage = input("Enter days and times when room in use (ex. Mon_18.00-19.00/Fri_16.00-15.00): ")
    try:
        conn.execute("insert into course_rooms values (%s, %s, '%s')" % (c_id, r_id, usage))
        print("\nAdded entry succesfully!\n")
    except Error as e:
        print("Error: ", e)

def add_course_teacher(conn):
    t_id = input("Teacher id: ")
    c_id = input("Course id: ")
    try:
        conn.execute("insert into course_teachers values (%s, %s)" % (t_id, c_id))
        print("\nAdded entry succesfully!\n")
    except Error as e:
        print("Error: ", e)

# Asks the user to commit changes and exits the program.
def end_program(conn):
    while True:
        commit = input("Commit changes to database? (y/n): ")
        if commit == "y":
            try:
                conn.commit()
                print("\nCommit succesful\n")
                sys.exit()
            except Error as e:
                print("Commit failed:",e)
                break
        elif commit == "n":
            print("\nDidn't commit changes\n")
            sys.exit()
        else:
            print("\nAnswer either 'y' or 'n'\n")
            break

main()
