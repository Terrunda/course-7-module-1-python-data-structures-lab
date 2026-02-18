# This module contains functions for filtering student data.

def filter_students_by_major(student_list, major):
    list_of_students = []

    for i in range(len(student_list)):
        if student_list[i][2] == major: #This searches through a tuple's major.
            list_of_students.append(student_list[i]) #The tuple is appended to the list.
    return list_of_students
    """
    Return a filtered list of students by major using a list comprehension.
    The function should:
    - Check if a student's major matches the given major (case insensitive).
    - Return a new list containing only students that match.
    """
