# Function to calculate grade based on average score
def calculate_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
         return 'F'

# Function to calculate total, average, and grade for each student
def calculate_student_grades():
    num_students = int(input("Enter the number of students: "))
    
    students_info = []

    # Loop to input each student's data
    for i in range (num_students):
        print(f"\nEnter information for student {i + 1}:")
        name = input("Enter student name: ")
        num_subjects = int(input("Enter the number of subjects: "))
        
        total_score = 0
        for j in range(num_subjects):
            score = float(input(f"Enter score for subject {j + 1}: "))
            total_score += score
        
        average_score = total_score / num_subjects
        grade = calculate_grade(average_score)

        # Store student info in a dictionary
        students_info.append({
            "name": name,
            "total_score ": total_score,
            "average_score": average_score,
            "grade": grade
        })
    
    # Print the results
    print("\nStudent Grades Summary:")
    print(f"{'Name.':<20}{'Total Score':<15}{'Average Score':<15}{'Grade'}")
    for student in students_info:
        print(f"{student['name']:<20}{student['total_score']:<15}{student['average_score']:<15.2f}{student['grade']}")
    
# Call the function to calculate grades
calculate_student_grades()
