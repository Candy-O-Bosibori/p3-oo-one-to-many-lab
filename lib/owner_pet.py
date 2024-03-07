class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all=[]
    def __init__(self, name, pet_type, owner=None ):
        self.name = name
        if pet_type not in self.PET_TYPES:
            raise ValueError("Pet type should be one of: " + ", ".join(self.PET_TYPES))
        self._pet_type = pet_type
        self._owner = owner
        self.all.append(self)

    @property
    def pet_type(self):
       return self._pet_type 
    
    @pet_type.setter
    def pet_type(self, value):
        if value not in self.PET_TYPES:
            raise ValueError("Invalid pet type")
        self._pet_type = value
         

    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self, value):
        if not isinstance(value, Owner) and not value:
            raise TypeError("Owner must be an instance of Ownerclass")
        self._owner = value


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
             raise TypeError("pet must be an instance of Pet class")
        pet.owner = self

    def get_sorted_pets(self):
        my_pets = [pet for pet in Pet.all if pet.owner == self]
        return sorted(my_pets, key=lambda x: x.name)


