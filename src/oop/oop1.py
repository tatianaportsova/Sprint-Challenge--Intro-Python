# Write classes for the following class hierarchy:

#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]

# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.

# e.g.
#
# class Whatever:
#     pass

# Put a comment noting which class is the base class

''' Base Class '''
class Vehicle:
    pass


''' Derived Class (from Vehicle)'''
class GroundVehicle(Vehicle):
    pass
''' Derived Class (from GroundVehicle)'''
class Car(GroundVehicle):
    pass
''' Derived Class (from GroundVehicle)'''
class Motorcycle(GroundVehicle):
    pass


''' Derived Class (from Vehicle)'''
class FlightVehicle(Vehicle):
    pass
''' Derived Class (from FlightVehicle)'''
class Airplane(FlightVehicle):
    pass
''' Derived Class (from FlightVehicle)'''
class Starship(FlightVehicle):
    pass
