# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   JBarnett,02/26/2025,Modified Script
# ------------------------------------------------------------------------------------------ #

# Import JSON Module
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data (TODO: Change this to a Dictionary)
students: list = []  # a table of student data
#csv_data: str = ''
json_data: str = ''
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.


# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
    file.close()

except Exception as e:
    print("Error: There was a problem reading the file.")
    print("Please check that your file exists in json format.")
    print("-- Technical Error Message --")
    print(e.__doc__)
    print(e.__str__())
finally:
#    if type(file) == "<class '_io.TextIDWrapper'>":
    if file.closed == False:
        file.close()

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!

        try:
            student_first_name = input("Enter the student's first name: ")
            # ErrorHandling
            if not student_first_name.isalpha():
                raise ValueError("ERROR: The student's first name must contain alphabetical characters.")
            student_last_name = input("Enter the student's last name: ")
            # ErrorHandling
            if not student_last_name.isalpha():
                raise ValueError("ERROR: The student's last name must contain alphabetical characters.")
            course_name = input("Please enter the name of the course: ")
            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            print(e) #prints custom message
            print("-- Technical Error Message --")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print("Error: There was a problem with the data you entered.")
            print("-- Technical Error Message --")
            print(e.__doc__)
            print(e.__str__())
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            print(f"student {student["FirstName"]} '"
                  f"{student["LastName"]} is enrolled in {student["CourseName"]}")
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file)
            file.close()
            print("The following data was saved to file!")
            for student in students:
                print(f"student {student["FirstName"]} '"
                  f"{student["LastName"]} is enrolled in {student["CourseName"]}")
        except Exception as e:
            print("Error: There was a problem reading the file.")
            print("Please check that the file exists in json format.")
            print("-- Technical Error Message --")
            print(e.__doc__)
            print(e.__str__())
        finally:
            if file.closed == False:
                file.close()
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
