# This module contains functions to process student data.

def format_student_data(student):
    student_id = student[0]
    student_name = student[1]
    student_major = student[2]

    student_string = f'ID: {str(student_id)} | Name: {student_name} | Major: {student_major}'
    return student_string
    """
    Format student data for display.
    The function should return a formatted string containing:
    - Student ID
    - Student Name
    - Major
    such as: "ID: 10 | Name: Louis Medina | Major: Computer Science"
    """

def display_students(student_list):
    for student in student_list:
        student_details = format_student_data(student)
        print(student_details)
    """
    Display all student records.
    Loop through the student_list and print each student using format_student_data().
    """