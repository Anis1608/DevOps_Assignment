student_data = {"anis":"A" , "Krishna":"B" , "Ravi":"C"}

def add_student_grade(name , grade):
    if name in student_data:
        print(f"Student {name} already exists with grade {student_data[name]}.")
    else:
        student_data[name] = grade
        print(f"Added student {name} with grade {grade}.")

def display_student_grades():
    if not student_data:
        print("No student data available.")
    else:
        print("Student Grades:")
        for i ,  (name, grade)in enumerate(student_data.items() , start=1):
            print(f"{i} . {name} : {grade}")

while True:
    print("Welcome to the Student Grade Management System...")
    try:
        print("1. Add Student Grade")
        print("2. Display Student Grades")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == "1":
            name = input("Enter student name: ")
            grade = input("Enter student grade: ")
            add_student_grade(name, grade)
        elif choice == "2":
            display_student_grades()
            continue_input = input("Do you want to continue? (Y/N): ")
            if continue_input.lower() not in ("y" , "yes"):
                 break
        elif choice == "3":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
   
    except Exception as e:
        print(f"An error occurred : {e}")




