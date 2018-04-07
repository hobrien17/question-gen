#6#
class CreditCard:
    def __init__(self, owner, balance):
        """Creates a new BankCard object

        Params:
            owner (str) : the name of the card's owner
            balance (float) : the card's current balance
        """
        self._owner = owner
        self._balance = balance

    def update_balance(self, value):
        """Add the given value to the card's balance"""
        self._balance += value

    def low_funds(self):
        return self._balance < 20

CreditCard("{name}", {float}) #creates a new instance of the CreditCard class under the variable {var} with owner {name} and balance ${float} #I#
update_balance({float}) #adds ${float} to the card {var}'s balance, assuming {var} has been correctly initialized #M#
update_balance({negfloat}) #removes ${posnegfloat} from the card {var}'s balance, assuming {var} has been correctly initialized #M#
CredicCard("{name}", {lowfloat}) #initializations will ensure the statement {var}.low_funds() returns True #B#