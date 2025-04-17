# import importlib
# pet_module = importlib.import_module("pet")
# Pet = getattr(pet_module, "Pet")

from pet import Pet 

my_pet = Pet("Spotty")
my_pet.get_status()
my_pet.eat()
my_pet.play()
my_pet.sleep()
my_pet.train("roll over")
my_pet.train("jump")
my_pet.show_tricks()
my_pet.get_status()
