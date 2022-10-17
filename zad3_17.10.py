# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 14:22:37 2022

@author: student
"""
class Property:
    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address
    
    def __str__(self):
        return f'{self.area}, {self.rooms}, {self.price}, {self.address}'
    

class House(Property):
    def __init__(self, area, rooms: int, price, address, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot
        
    def __str__(self):
        return super().__str__() + f' {self.plot}'

class Flat(Property):
    def __init__(self, area, rooms: int, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor
        
    def __str__(self):
        return f'{self.floor}'
House1 = House("Paderewskiego",2,"123","Bogucicka 7",5)
Flat1 = Flat("Ligota",3,"123","3 Maja 5b",6)
print(House1)