# This module contains operations related to sets.

def unique_majors(student_list):
    student_major_list = []
    for student in student_list:
        print(student)
        student_major = student[2]
        print(student_major)
        student_major_list.append(student_major)

    unique_major_set = set(student_major_list)
    return unique_major_set

    """
    Return a set of unique student majors using set comprehension.
    Extract the major field from each student record.
    """
