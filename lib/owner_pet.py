class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet_type: {pet_type}. Must be one of {Pet.PET_TYPES}.")
        self.pet_type = pet_type
        self._owner = None
        if owner:
            if not isinstance(owner, Owner):
                raise Exception("Owner must be an instance of the Owner class.")
            self.owner = owner
        Pet.all.append(self)

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        if not isinstance(value, Owner):
            raise Exception("Owner must be an instance of the Owner class.")
        self._owner = value

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("The pet must be an instance of the Pet class.")
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)
