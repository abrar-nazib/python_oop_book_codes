def get_valid_input(input_string, valid_options):
    input_string += " ({}) ".format(", ".join(valid_options))
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response


class Property:
    def __init__(self, square_feet: int = 0, beds: int = 0, baths: int = 0, **kwargs):
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths

    def display(self):
        print("PROPERTY DETAILS")
        print("================")
        print(f"Area: {self.square_feet} Sq Ft")
        print(f"Bedrooms: {self.num_bedrooms}")
        print(f"Bathrooms: {self.num_baths}")

    @staticmethod
    def prompt_init():
        return dict(
            square_feet=int(input("Enter the square feet: ")),
            beds=int(input("Enter number of bedrooms: ")),
            baths=int(input("Enter number of baths: ")),
        )


class Apartment(Property):
    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")

    def __init__(self, balcony: str = "", laundry: str = "", **kwargs):
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        super().display()
        print("\nApartment Details")
        print("=================")
        print(f"Laundry: {self.laundry}")
        print(f"Balcony: {self.balcony}")

    @staticmethod
    def prompt_init():
        parent_init = Property.prompt_init()
        laundry = get_valid_input(
            "What laundry faciliteis does the property have?", Apartment.valid_laundries
        )
        balcony = get_valid_input(
            "Does the property have a balcony?", Apartment.valid_balconies
        )

        parent_init.update(
            {"laundry": laundry, "balcony": balcony}
        )  # Update the existing dictionary
        return parent_init


class House(Property):
    valid_garage = ("attached", "detached", "none")
    valid_fenced = ("yes", "no")

    def __init__(
        self, num_stories: int = 1, garage: str = "", fenced: str = "", **kwargs
    ):
        super().__init__(**kwargs)
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories

    def display(self):
        super().display()
        print("\nHouse Details")
        print("=============")
        print(f"# of stories: {self.num_stories}")
        print(f"Garage: {self.garage}")
        print(f"Fenced: {self.fenced}")

    @staticmethod
    def prompt_init():
        parent_init = Property.prompt_init()
        fenced = get_valid_input("Is the yard fenced?", House.valid_fenced)
        garage = get_valid_input("Is there a garage?", House.valid_garage)
        num_stories = int(input("How many stories? "))
        parent_init.update(
            {"fenced": fenced, "garage": garage, "num_stories": num_stories}
        )
        return parent_init


class Purchase:
    def __init__(self, price: int = 0, taxes: int = 0, **kwargs):
        self.price = price
        self.taxes = taxes

    def display(self):
        super().display()  # Will be utilized as a mixin
        print("\nPurchase Details")
        print("================")
        print(f"Price: {self.price}")
        print(f"Taxes: {self.taxes}")

    @staticmethod
    def prompt_init():
        return dict(
            price=int(input("What is the selling price? ")),
            taxes=int(input("What are the estimated taxes? ")),
        )


class Rental:
    def __init__(self, furnished="", utilities="", rent="", **kwargs):
        super().__init__(**kwargs)
        self.furnished = furnished
        self.utilities = utilities
        self.rent = rent

    def display(self):
        super().display()  # No superclass but still calling it because it will be utilized as a mixin
        print("\nRental Details")
        print("=============")
        print(f"Rent: {self.rent}")
        print(f"Utilities: {self.utilities}")
        print(f"Furnished: {self.furnished}")

    @staticmethod
    def prompt_init():
        return dict(
            rent=input("What is the monthly rent? "),
            utilities=input("What are the estimated utilities? "),
            furnished=get_valid_input("Is the property furnished? ", ("yes", "no")),
        )


class HouseRental(Rental, House):
    @staticmethod
    def prompt_init():
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init


if __name__ == "__main__":
    init = HouseRental.prompt_init()
    house = HouseRental(**init)
    house.display()
