# add your Student class here!
class Student:

    def __init__(self, name, grade, classes):
        self.name = name
        self.grade = grade
        self.classes = classes

    def add_class(self, new_class):
        # if not new_class:
        #     return None
        classes = self.classes.append(new_class)
        return classes

    def get_num_classes(self):
        total_class = len(self.classes)
        return total_class

    def summary(self):
        return(f"{self.name} is a {self.grade} enrolled in {self.get_num_classes()} classes")
