# Import Fan class from Fan_properties
from Fan_properties import Fan

# Create class for TestFan
class TestFan:
    def implement(self):
    # Create two fans
        fan1 = Fan(Fan.FAST, True, 10, "Yellow")
        fan2 = Fan(Fan.MEDIUM, False, 5, "Blue")

# Print properties of first fan
        print("1st Fan's Properties:")
        print("Speed:", fan1.get_speed())
        print("Switch:", fan1.get_switch())
        print("Radius:", fan1.get_radius())
        print("Color:", fan1.get_color())

# Print properties of second fan
        print("2nd Fan's Properties:")
        print("Speed:", fan2.get_speed())
        print("Switch:", fan2.get_switch())
        print("Radius:", fan2.get_radius())
        print("Color:", fan2.get_color())

# Create instance of TestFan 
if __name__ == "__main__":
    test_fans = TestFan()
# Run with implement method
    test_fans.implement()