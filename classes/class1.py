#6#
class GoCard:
    def __init__(self, user, balance):
        """Creates a new GoCard object

        Params:
            user (str) : the name of the card's owner
            balance (float) : the card's current balance
        """
        self._user = user
        self._balance = balance

    def get_user(self): #1X#
        """(str) Return the card's user""" #1X#
        return self._user #1R#

    def get_balance(self): #2X#
        """(float) Return the card's balance""" #2X#
        return self._balance #2R#

    def update_balance(self, value): #3X#
        """Add the given value to the card's balance""" #3X#
        self._balance += value #3O#

    def detract_balance(self, value): #4X#
        """Substract the given value from the card's balance""" #4X#
        self._balance -= value #4O#

    def low_balance(self): #5X#
        """(bool) Return true if the balance is less than 5, otherwise return false""" #5X#
        return self._balance < 5 #5B#

    def valid_balance(self): #6X#
        """(bool) Return true if the balance is 0 or more, otherwise return false""" #6X#
        return self._balance >= 0 #6B#

GoCard("{name}", {float}) #creates a new instance of the GoCard class under the variable {var} #00I#
update_balance({float}) #updates the balance by ${float}, assuming {var} has been correctly initialized #30M#
detract_balance({float}) #removes ${float} from the balance, assuming {var} has been correctly initialized #40M#