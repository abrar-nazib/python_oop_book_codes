class Inventory:
    def lock(self, item_type):
        """Select the type of item that is going to be manipulated. This method will lock the item so no one else can access it until it's unlocked. It will prevent selling the same item to two different customers."""

        pass

    def unlock(self, item_type):
        """Release the given type so that other customers can access it."""
        pass

    def purchase(self, item_type):
        """If the item is not locked, raise an exception. If the item_type does not exist, raise an exceptionl. If the item is currently out of stock, raise an exception. If the item is available, subtract one item and return the number of items left."""
        pass


item_type = "widget"
inv = Inventory()
inv.lock(item_type)

try:
    num_left = inv.purchase(item_type)

except InvalidItemType:
    print(f"Sorry, we don't sell {item_type}")
except OutOfStock:
    print(f"Sorry, {item_type} is out of stock")
else:
    print(f"Purchase complete. There are {num_left} {item_type} left")
finally:  # Release the item back either way.
    inv.unlock(item_type)
