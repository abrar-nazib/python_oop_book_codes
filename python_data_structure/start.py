from collections import namedtuple

stocks = {"GOOG": (613.30, 625.86, 610.50), "MSFT": (30.25, 30.70, 30.19)}

stocks.setdefault("GOOG", "INVALID")  # Doesn't change anything
print(stocks.get("GOOG"))
stocks.setdefault("APPL", "INVALID")
print(stocks.get("APPL"))
print(stocks)

print(stocks.keys())  # Returns dict_keys in an array
print(stocks.values())  # Returns dict_values in an array


print(stocks.items())  # Returns tupled dict items as (key, value)
for stock, values in stocks.items():
    print(f"{stock} last value is {values[0]}")


random_keys = {}
random_keys["astring"] = "somestring"
random_keys[5] = "aninteger"
random_keys[25.2] = "floats work too"
random_keys[("abc", 123)] = "so do tuples"


class AnObject:
    def __init__(self, avalue):
        self.avalue = avalue


my_object = AnObject(14)

random_keys[my_object] = "We can even store objects"
my_object.avalue = 12
try:
    random_keys[[1, 2, 3]] = "we can't store lists though"
except:
    print("unable to store list\n")
for key, value in random_keys.items():
    print("{} has value {}".format(key, value))
