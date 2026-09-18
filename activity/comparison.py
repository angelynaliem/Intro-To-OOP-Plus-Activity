
def get_student_with_more_classes(student_one, student_two):

    classes_one = student_one.get_num_classes()
    classes_two = student_two.get_num_classes()

    if classes_one > classes_two:
        return student_one.name
    
    elif classes_one == classes_two:
        if classes_one == 0 and classes_two == 0:
            return "Both students do not have classes"
        else:
            return f"{student_one.name} and {student_two.name}"

    return student_two.name