# Import Car class
from Car_properties import Car

# Create class for testing 
class CarTest:
    def __init__(self):
        self.car = Car(1967, "Volkswagen")

    def implement(self):
    # Loop to accelerate and break five times
        for i in range(5):
            self.car.accelerate()
            print("Current speed:", self.car.get_speed())

        for i in range(5):
            self.car.brake()
            print("Current speed:", self.car.get_brake())

# Create an instance for CarTest
car_test = CarTest()
# Implement 
car_test.implement()