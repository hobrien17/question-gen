class Website:
    def __init__(self, owner, visitors):
        """Creates a new Website object

        Params:
            owner (str) : the name of the owner of the website
            visitors (float) : the website's annual visitors, in thousands
        """
        self._owner = owner
        self._visitors = visitors

    def increase_visitors(self, visitors):
        self._visitors += visitors

    def is_popular(self):
        return self._visitors >= 20

Website("{name}", {float}) #correctly creates a new instance of the Website class under the variable {var} with owner {name} and visitors {float} #I#
increase_visitors({float}) #correctly increases the website {var}'s visitors by {float}, assuming {var} has been correctly initialized #M#
increase_visitors({negfloat}) #correctly decreases the website {var}'s visitors by {float}, assuming {var} has been correctly initialized #M#
Website("{name}", {lowfloat}) #initializations will ensure the statement {var}.is_popular() returns False #B#