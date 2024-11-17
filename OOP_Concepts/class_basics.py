class Car:
    """A simple attempt to represent a car"""
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
    
    def get_descriptive_name(self):
        """Return a neatly formatted name"""
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title() 
    
    def display_info(self):
        """Display car information in a detailed format"""
        print(f"Car Information: {self.get_descriptive_name()}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print()  # Adds a blank line for better readability


# Creating instances of Car
my_new_car1 = Car('audi', 'a4', 2005)
my_new_car2 = Car('benz', 'camry', 2010)

#calling display_info() to test functionality
my_new_car1.display_info()
my_new_car2.display_info()







     