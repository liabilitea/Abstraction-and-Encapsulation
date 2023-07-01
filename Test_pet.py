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
        name = input("Please enter the name of your pet: ")
        pet.set_name(name)

        animal_type = input("Please enter what type of animal your pet is: ")
        pet.set_animal_type(animal_type)
    
        age = input("Please enter the current age of your pet: ")
        pet.set_age(age)

    # Create header for Pet Details
        print("\nPet Details:")
    # Display pet details
        print("Name: ", (pet.get_name()))
        print("Type: ", (pet.get_animal_type()))
        print("Age: ", (pet.get_age()))


# Create instance for PetTest class
pet_test = PetTest()
# Implement
pet_test.implement()