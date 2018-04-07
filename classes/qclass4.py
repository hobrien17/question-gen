class Country:
    def __init__(self, name, population):
        """Creates a new Country object

        Params:
            name (str) : the name of the country
            population (float) : the country's population, in millions
        """
        self._name = name
        self._population = population

    def increase_population(self, population):
        self._population += population

    def high_population(self):
        return self._population >= 20

Country("{country}", {float}) #correctly creates a new instance of the Country class under the variable {var} with name {country} and population {float} #I#
increase_population({float}) #correctly adds {float} to the country {var}'s population, assuming {var} has been correctly initialized #M#
increase_population({negfloat}) #correctly subtracts ${posnegfloat} from the country {var}'s population, assuming {var} has been correctly initialized #M#
Country("{country}", {highfloat}) #initializations will ensure the statement {var}.high_population() returns True #B#