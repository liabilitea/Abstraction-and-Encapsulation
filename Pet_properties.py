# Create class named Pet
class Pet:
    # Create constructor to initialize attributes
    def __init__(self):
        self.__name = ''
        self.__animal_type = ''
        self.__age = 0

# Create mutator methods
    # Name
    def set_name(self, name):
        self.__name = name

    # Type
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    # Age
    def set_age(self, age):
        self.__age = age

# Create accessor methods
    # Name
    def get_name(self):
        return self.__name 

    # Type
    def tet_animal_type(self):
        return self.__animal_type
    
    # Age
    def get_age(self):
        return self.__age