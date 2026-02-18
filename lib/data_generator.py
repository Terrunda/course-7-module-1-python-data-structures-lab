# This module contains functions to lazily generate student data.

def student_generator(student_list, major):

    generator_expression = (student for student in student_list if student[2] == major) #The genrator expression returns an experession for students BY major.
    return generator_expression
    """
    Generate student records filtered by major lazily for memory efficiency
    using a Python generator.
    """
    pass
