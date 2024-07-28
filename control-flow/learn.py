# Define a Student class

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # This method shows the name of the student
    def callname(self):
        print(f"My name is {self.name}")

    # This method shows the age of the student
    def callage(self):
        print(f"My age is {self.age}")


randal = Student("Kato", 24)

randal.callname()
randal.callage()


# # Define the Dog class
# class Dog:
#     # This is the constructor method, called when we create a new Dog object
#     def __init__(self, name, breed):
#         self.name = name  # Set the name of the dog
#         self.breed = breed  # Set the breed of the dog

#     # This method makes the dog bark
#     def bark(self):
#         print(f"{self.name} says Woof!")

#     # This method makes the dog sit
#     def sit(self):
#         print(f"{self.name} sits down.")
    
#     # This method makes the dog roll over
#     def roll_over(self):
#         print(f"{self.name} rolls over.")

# # Function to get user input and create a Dog object
# def create_dog():
#     name = input("Enter the dog's name: ")
#     breed = input("Enter the dog's breed: ")
#     return Dog(name, breed)

# # Create a Dog object using user input
# dog = create_dog()

# # Make the dog bark, sit, and roll over
# dog.bark()
# dog.sit()
# dog.roll_over()
