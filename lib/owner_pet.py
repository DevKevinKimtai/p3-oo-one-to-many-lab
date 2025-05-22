class Owner:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        self.name = name
        self._pets = []

    def pets(self):
        return self._pets

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Can only add Pet instances")
        pet.owner = self
        if pet not in self._pets:
            self._pets.append(pet)

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []

    def __init__(self, name, pet_type, owner=None):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        if pet_type not in self.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}")
        
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, owner):
        if owner is not None and not isinstance(owner, Owner):
            raise Exception("Owner must be an Owner instance")
        
        # Remove from previous owner's pet list
        if hasattr(self, '_owner') and self._owner is not None:
            self._owner._pets.remove(self)
        
        # Set new owner
        self._owner = owner
        
        # Add to new owner's pet list
        if owner is not None and self not in owner._pets:
            owner._pets.append(self)