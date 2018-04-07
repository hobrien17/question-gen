class Staff:
    def __init__(self, name, wage):
        """Creates a new Staff object

        Params:
            name (str) : the name of the staff member
            wage (float) : the staff member's hourly wage
        """
        self._name = name
        self._wage = wage

    def change_wage(self, value):
        self._wage += value

    def low_salary(self):
        return self._wage < 20

Staff("{name}", {float}) #correctly creates a new instance of the Staff class under the variable {var} with name {name} and wage {float} #I#
change_wage({float}) #correctly adds {float} to the staff member {var}'s wage, assuming {var} has been correctly initialized #M#
change_wage({negfloat}) #correctly subtracts ${posnegfloat} from the staff member {var}'s wage, assuming {var} has been correctly initialized #M#
Staff("{name}", {highfloat}) #initializations will ensure the statement {var}.low_salary() returns False #B#