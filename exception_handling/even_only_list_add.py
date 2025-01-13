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


if __name__ == "__main__":
    exception_runner()
