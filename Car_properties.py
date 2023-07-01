# Import termcolor for colored output

# Create a class named Car
class Car:
    # Create a constructor to initialize Car's attributes
    def __init__(self, year, make):
        self.__year = year
        self.__make = make
        self.__speed = 0

    # Create methods
    # Accelerate +5
    def accelerate(self):
        # Add color
        print("Accelerating...")
        self.__speed += 5

    # Brake -5
    def brake(self):
        # Add color
        print("Braking...")
        self.__speed -= 5 

    # Current Speed
    def get_speed(self):
        return self.__speed

