# Import modules for output design
import pyfiglet
from termcolor import colored

# Import Car class
from Car_properties import Car

# Create class for testing 
class CarTest:
    def __init__(self):
        self.car = Car(1967, "Volkswagen")

    def implement(self):
    # Create a header with pyfiglet
        speed_header = pyfiglet.figlet_format("Car Speed", font = "serifcap")
        header_color = colored(speed_header, color = 'light_red')
    # Print header
        print(header_color)

    # Loop to accelerate and break five times
        for i in range(5):
            self.car.accelerate()
            print("Current speed:", self.car.get_speed())
            # Add line each iteration for clean output
            print()

        for i in range(5):
            self.car.brake()
            print("Current speed:", self.car.get_speed())
            # Add line each iteration for clean output
            print()
            
# Create an instance for CarTest
car_test = CarTest()
# Implement 
car_test.implement()