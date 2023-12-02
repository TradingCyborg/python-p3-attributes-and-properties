#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self):
        self.name = None

@property
def name(self):
    return self.name
@name.setter
def name(self, value):
    if isinstance(value, str) and len(value) > 25:
        print("Name must be a string under 25 characters.")
    else:
        self.name = value.title()
