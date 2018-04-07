#6#
class Student:
    def __init__(self, student_num, name, courses):
        """Creates a new Student object

        Params:
            student_num (int) : the student's ID
            name (str) : the student's name
            courses (list[str]) : the courses the student is taking
        """
        self._student_num = student_num
        self._name = name
        self._courses = courses

    def get_student_num(self): #1X#
        """(int) Return the person's student number""" #1X#
        return self._student_num #1R#

    def get_courses(self): #2X#
        """(list[str]) Return the student's courses""" #2X#
        return self._courses #2R#

    def add_course(self, course): #3X#
        """Add the given course to the student's courses""" #3X#
        self._courses.append(course) #3O#

    def drop_course(self, title): #4X#
        """Remove the given course from the student's courses""" #4X#
        self._courses.remove(course) #4O#

    def is_valid_num(self): #5X#
        """(bool) Return true if the student's number has 8 digits, otherwise false""" #5X#
        return len(str(self._student_num)) == 8 #5B#

    def is_part_time(self): #6X#
        """(bool) Return true if the students is enrolled in 2 or less courses""" #6X#
        return len(self._courses) <= 2 #6B#