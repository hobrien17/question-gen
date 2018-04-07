#6#
class Player:
    def __init__(self, name, health):
        """Creates a new Player object

        Params:
            name (str) : the player's name
            health (int) : the player's health
        """
        self._name = name
        self._health = health

    def get_name(self): #1X#
        """(str) Return the player's name""" #1X#
        return self._name #1R#

    def get_health(self): #2X#
        """(int) Return the player's health""" #2X#
        return self._health #2R#

    def heal(self, amount): #3X#
        """Add the given amount to the player's health""" #3X#
        self._health += amount #3O#

    def take_damage(self, damage): #4X#
        """Substract the given damage from the player's health""" #4X#
        self._health -= damage #4O#

    def is_alive(self): #5X#
        """(bool) Return true if the player's health is above 0, otherwise return false""" #5X#
        return self._health > 0 #5B#

    def valid_name(self): #6X#
        """(bool) Return true if the player's name is only made up of alphabetic characters""" #6X#
        return self._name.isalpha() #6B#