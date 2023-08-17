from copy import deepcopy

class Laptop():
    def __init__(self, model):
        self.model : int = model

class Person():
    def __init__(self, name, model):
        self.name : str = name
        self.laptop : Laptop = Laptop(model)
    
sam = Person("sam", 14)
samsam = deepcopy(sam)
print(f"sam's: {repr(sam.laptop)}")
print(f"copy's: {repr(samsam.laptop)}")
print(samsam.laptop.model)
