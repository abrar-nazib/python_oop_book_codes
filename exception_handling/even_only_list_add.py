import random


class EvenOnly(list):
    def append(self, integer):
        if not isinstance(integer, int):
            raise TypeError("Only integers can be added")
        if integer % 2:
            raise ValueError("Only even numbers can be added")
        super().append(integer)


def no_return():
    print("I am about to raise an exception")
    raise Exception("This is always raised")
    print("This line is never executed")
    return "I won't be returned"


def exception_runner():
    print("Going to call the no_return function")
    no_return()
    print("This is not supposed to run")


def funny_division(divider):
    try:
        return 100 / divider

    except ZeroDivisionError:
        return "Zero is not a good idea"


def funny_division_multi_catch(divider):
    try:
        if divider == 13:
            raise ValueError("13 is an unlucky number")
        return 100 / divider
    except (ZeroDivisionError, TypeError):
        return "Enter a number which is not zero"


def funny_division_separate_catch(divider):
    try:
        if divider == 13:
            raise ValueError("13 is an unlucky number")
        return 100 / divider
    except ZeroDivisionError:
        return "Can't divide by zero"
    except TypeError:
        return f"Can't divide number with {type(divider).__name__}"
    except ValueError:
        print("No! No! No! Not 13")
        raise


def exception_hierarchy():
    some_exceptions = [
        ValueError,
        ZeroDivisionError,
        TypeError,
        NameError,
        IndexError,
        None,
    ]

    try:
        choice = random.choice(some_exceptions)
        print(f"Raising {choice}")
        if choice:
            raise choice("Yooo Lottery Lag gayi")
    except ValueError:
        print("Caught value error")
    except ZeroDivisionError:
        print("Caught Zero Division Error")
    except TypeError:
        print("Caught type error")
    except NameError:
        print("Caught Name Error")
    except IndexError:
        print("Caught Index Error")
    else:
        print("No error was caught")
    finally:
        print("This line will run regardless")


class InvalidWithdrawal(Exception):
    def __init__(self, balance, amount):
        # Calling super with the message to be displayed
        super().__init__(
            f"Account balance ${balance} is less than withdrawal amount ${amount}"
        )
        self.amount = amount
        self.balance = balance

    @property
    def overage(self):
        return self.amount - self.balance


if __name__ == "__main__":
    try:
        raise InvalidWithdrawal(25, 55)
    except InvalidWithdrawal as e:
        print(
            f"I'm sorry, but your withdrawal is more than your balance by ${e.overage}"
        )
