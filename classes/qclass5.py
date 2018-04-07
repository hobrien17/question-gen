class Car:
    def __init__(self, manufacturer, price):
        """Creates a new Car object

        Params:
            manufacturer (str) : the name of the car
            price (float) : the car's price, in thousands
        """
        self._manufacturer = manufacturer
        self._price = price

    def raise_price(self, value):
        self._price += value

    def is_bargin(self):
        return self._price < 20

Car("{car}", {float}) #correctly creates a new instance of the Car class under the variable {var} with manufacturer {car} and price ${float} #I#
raise_price({float}) #correctly increases the car {var}'s price by ${float}, assuming {var} has been correctly initialized #M#
raise_price({negfloat}) #correctly decreases the car {var}'s price by ${float}, assuming {var} has been correctly initialized #M#
Car("{car}", {highfloat}) #initializations will ensure the statement {var}.is_bargin() returns False #B#