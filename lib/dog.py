#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self):
        self._name = None

    def name(self):
        return self._name
    
    def name(self, value):
        if not isinstance(value, str) or not (1 <= len(value <= 25)):
            print("Name must be a stringg between 1 and 25 characters.")
        
    def breed(self, value):
        if value not in self.APPROVED_BREEDS:
            print("Breed must be in the list of approved breeds.")
        else:
            self._breed = value 
