# Import Fan class from Fan_properties
from Fan_properties import Fan

#Import modules for design
import pyfiglet
from termcolor import colored

# Create class for TestFan
class TestFan:
    def implement(self):
    # Create two fans
        fan1 = Fan(Fan.FAST, True, 10, "Yellow")
        fan2 = Fan(Fan.MEDIUM, False, 5, "Blue")

# Add heading using imported design modules
        property_header = pyfiglet.figlet_format("Fan Properties", font = "bubble")
        header_color = colored(property_header, color = 'green')
# Print heading
        print(header_color)

# Add colors to texts
# Print properties of first fan
        print(colored("1st Fan's Properties:", 'magenta'))
        print("Speed:", colored(fan1.get_speed(), 'yellow'))
        print("Switch:", colored(fan1.switch_value(), 'yellow'))
        print("Radius:", colored(fan1.get_radius(), 'yellow'))
        print("Color:", colored(fan1.get_color(), 'yellow'))

# Add colors to texts
# Print properties of second fan
        print(colored("\n2nd Fan's Properties:", 'magenta'))
        print("Speed:", colored(fan2.get_speed(), 'cyan'))
        print("Switch:", colored(fan2.switch_value(), 'cyan'))
        print("Radius:", colored(fan2.get_radius(), 'cyan'))
        print("Color:", colored(fan2.get_color(), 'cyan'))

# Create instance of TestFan 
if __name__ == "__main__":
    test_fans = TestFan()
# Run with implement method
    test_fans.implement()