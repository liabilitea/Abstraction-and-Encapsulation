# Create Fan class
class Fan:

    # Create a constructor, set as default
    def __init__(self, speed=1, On=False, radius=5, color='Blue'):
    # All properties should be private
        self.__speed = speed
        self.__on = On
        self.__radius = radius
        self.__color = color

# Define speed property
    SLOW = 1
    MEDIUM = 2
    FAST = 3

# Create accessor methods to get values
    # Speed
    def get_speed(self):
        return self.__speed
    # Switch, on and off
    def get_switch(self):
        return self.__on
    
    def switch_value(self):
        return "On" if self.__on else "Off"
    # Radius
    def get_radius(self):
        return self.__radius
    # Color
    def get_color(self):
        return self.__color
    
# Create mutator methods to modify values
    # Speed
    def set_speed(self, speed):
        self.__speed = speed   
    # Switch On
    def turn_on(self):
        self.__on = True
    # Switch Off
    def turn_off(self):
        self.__on = False
    # Radius
    def set_radius(self, radius):
        self.__radius = radius
    # Color
    def set_color(self, color):
        self.__color = color