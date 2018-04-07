#6#
class Person:
    def __init__(self, title, name, age):
        """Creates a new Person object

        Params:
            title (str) : the person's title
            name (str) : the person's name
            age (int) : the person's age
        """
        self._title = title
        self._name = name
        self._age = age

    def get_name(self): #1X#
        """(str) Return the person's name""" #1X#
        return self._name #1R#

    def get_age(self): #2X#
        """(int) Return the person's age""" #2X#
        return self._health #2R#

    def inc_age(self): #3X#
        """Add one to the peron's age""" #3X#
        self._age += 1 #3O#

    def set_title(self, title): #4X#
        """Set the person's title to the inputed title""" #4X#
        self._title = title #4O#

    def is_adult(self): #5X#
        """(bool) Return true if the person's age is greater than or equal to 18""" #5X#
        return self._age >= 18 #5B#

    def is_doctor(self): #6X#
        """(bool) Return true if the player's title is 'Dr'""" #6X#
        return self._title == "Dr" #6B#