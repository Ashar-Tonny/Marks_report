#!/usr/bin/env python3
import pandas as pd
print("\t\t\t\t\t\t\t\tUMEZO PRIMARY SCHOOL\n")
# Initial data for the DataFrame
data = {
    "Student Id": ["STU001", "STU002", "STU003", "STU004", "STU005"],
    "First Name": ["Johson", "Jack", "Alphones", "Robert", "Catherine"],
    "Second Name": ["Dophus", "Smith", "Mutie", "Jayson", "Wambui"],
    "Sex":["Male","Male","Male","Male","Female"],
    "Mathematics": [85, 90, 78, 92, 82],
    "English": [76, 88, 82, 79, 85],
    "Kiswahili": [80, 85, 70, 84, 77],
    "CRE": [92, 78, 85, 83, 90],
    "History": [81, 83, 75, 86, 89],
    "Biology": [87, 89, 81, 91, 83],
    "Physics": [79, 82, 88, 85, 90],
    "Chemistry": [85, 87, 80, 89, 86],
    "Geography": [88, 87, 85, 82, 86],
    "Business Studies": [83, 86, 89, 80, 87],
    "Agriculture": [91, 84, 83, 85, 87]
}

# Create the DataFrame
students_df = pd.DataFrame(data)
students_df["Average"]=(students_df["Mathematics"] + students_df["English"] + students_df["Kiswahili"] + students_df["CRE"] + students_df["History"] + students_df["Biology"] + students_df["Physics"] + students_df["Chemistry"] + students_df["Geography"] + students_df["Business Studies"] + students_df["Agriculture"])/11
# Function to display marks of a specific student by Student Id
def display_student_marks(student_id):
    if student_id in students_df["Student Id"].values:
        student_details = students_df[students_df["Student Id"] == student_id]
        print("\nStudent Details:")
        print(student_details)
    else:
        print(f"\nStudent with ID {student_id} not found.")

# Function to add a new student
def add_student():
    global students_df
    print("\n\t\t\t\tENTER THE DETAILS OF THE NEW STUDENT")
    student_id = input("Student Id: ")

    # Check if the student ID already exists
    if student_id in students_df["Student Id"].values:
        print("\nA student with this ID already exists.")
        return

    first_name = input("First Name: ")
    second_name = input("Second Name: ")
    Gender=input("Sex:")
    mathematics = int(input("Mathematics: "))
    english = int(input("English: "))
    kiswahili = int(input("Kiswahili: "))
    cre = int(input("CRE: "))
    history = int(input("History: "))
    biology = int(input("Biology: "))
    physics = int(input("Physics: "))
    chemistry = int(input("Chemistry: "))
    geography = int(input("Geography: "))
    business_studies = int(input("Business Studies: "))
    agriculture = int(input("Agriculture: "))

    # Create a new row as a dictionary
    new_student = {
        "Student Id": student_id,
        "First Name": first_name,
        "Second Name": second_name,
        "Sex":Gender,
        "Mathematics": mathematics,
        "English": english,
        "Kiswahili": kiswahili,
        "CRE": cre,
        "History": history,
        "Biology": biology,
        "Physics": physics,
        "Chemistry": chemistry,
        "Geography": geography,
        "Business Studies": business_studies,
        "Agriculture": agriculture
    }

    # Adding the new student to the DataFrame
    students_df=pd.concat([students_df,pd.DataFrame([new_student])],ignore_index=True)
    print("\nNew student added successfully!")
    students_df = pd.DataFrame(data)
    students_df["Average"]=(students_df["Mathematics"] + students_df["English"] + students_df["Kiswahili"] + students_df["CRE"] + students_df["History"] + students_df["Biology"] + students_df["Physics"] + students_df["Chemistry"] + students_df["Geography"] + students_df["Business Studies"] + students_df["Agriculture"])/11

def View_All():
    counting=students_df["Student Id"].count()
    #print(students_df.pivot(index=["Student Id","First Name","Second Name"],values=["Mathematics","English","Kiswahili","CRE","History","Biology","Physics","Chemistry","Geography","Business Studies","Agriculture"],columns="Sex"))
    print(students_df.head(counting))

# Main program loop
while True:
    print("\nMenu:")
    print("1. View Student Performance")
    print("2. Add a New Student")
    print("3.View All")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        student_id = input("\nEnter Student Id to view performance: ")
        display_student_marks(student_id)
    elif choice == "2":
        add_student()
    elif choice=="3":
        View_All()
    elif choice == "4":
        print("\nExiting the program. Goodbye!")
        break
    else:
        print("\nInvalid choice. Please try again.")
