#Import modules for output design
import pyfiglet
from termcolor import colored

# Import Pet class
from Pet_properties import Pet

# Create class for PetTest
class PetTest:
    # Create method to run the display
    def implement(self):
    # Create object for the Pet class
        pet = Pet()

    # Create header for Pet Survey 
        survey_header = pyfiglet.figlet_format("Pet Survey", font = "larry3d")
        survey_color = colored(survey_header, color = 'magenta')
        print(survey_color)
    
    # Prompt user to enter pet details
    # Add colors to the questions
        name = input(colored("Please enter the name of your pet: ", 'light_blue'))
        pet.set_name(name)

        animal_type = input(colored("Please enter what type of animal your pet is: ", 'light_blue'))
        pet.set_animal_type(animal_type)
    
        age = input(colored("Please enter the current age of your pet: ", 'light_blue'))
        pet.set_age(age)

    # Create header for Pet Details
        details_header = pyfiglet.figlet_format("Pet Details", font = "bubble")
        details_color = colored(details_header, color = 'red')
        print(details_color)
    
    # Display pet details
        print(colored("Name: ", 'yellow'), colored(pet.get_name(), color = 'green'))
        print(colored("Type: ", 'yellow'), colored(pet.get_animal_type(), color = 'green'))
        print(colored("Age: ", 'yellow'), colored(pet.get_age(), color = 'green'))


# Create instance for PetTest class
pet_test = PetTest()
# Implement
pet_test.implement()