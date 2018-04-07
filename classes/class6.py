#6#
class Store:
    def __init__(self, name, stock):
        """Creates a new Store object

        Params:
            name (str) : the name of the store
            stock (list[str]) : the current in-store stock
        """
        self._name = name
        self._stock = stock

    def get_name(self): #1X#
        """(str) Return the name of the store""" #1X#
        return self._name #1R#

    def get_stock(self): #2X#
        """(list[str]) Return the store's stock""" #2X#
        return self._stock #2R#

    def add_stock(self, extra_stock): #3X#
        """Add all of the given extra stock to the current store's stock""" #3X#
        self._stock.extend(extra_stock) #3O#

    def remove_item(self, item): #4X#
        """Remove the given item from the store's stock""" #4X#
        self._stock.remove(item) #4O#

    def has_stock(self): #5X#
        """(bool) Return true if there are more than 0 items of stock in the store, otherwise return false""" #5X#
        return len(self._stock) > 0 #5B#

    def is_full(self): #6X#
        """(bool) Return true there are exactly 100 items of stock in the store, otherwise return false""" #6X#
        return len(self._stock) == 100 #6B#