#6#
class Course:
    def __init__(self, course_code, course_title, students_enrolled):
        """Creates a new Course object

        Params:
            course_code (str) : the course's code
            course_title (str) : the name of the course
            students_enrolled (int) : the number of students enrolled
        """
        self._code = course_code
        self._title = course_title
        self._enrolled = students_enroller

    def get_course_code(self): #1X#
        """(str) Return the course's code""" #1X#
        return self._code #1R#

    def get_course_title(self): #2X#
        """(str) Return the course's title""" #2X#
        return self._title #2R#

    def enrol_student(self, course): #3X#
        """Increment the students enrolled by 1""" #3X#
        self._enrolled += 1 #3O#

    def change_title(self, new_title): #4X#
        """Change the course's title to the given title""" #4X#
        self._title = new_title #4O#

    def can_run(self): #5X#
        """(bool) Return true if there are 10 or more students enrolled, otherwise return false""" #5X#
        return students_enrolled >= 10 #5B#

    def is_large_course(self): #6X#
        """(bool) Return true if the there are over 100 students enrolled, otherwise return false""" #6X#
        return students_enrolled > 100 #6B#