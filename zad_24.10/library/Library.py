# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 14:17:06 2022

@author: student
"""


    
class Library:
    def __init__(self, city, street, zip_code, open_hours,phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone
     
    def __str__(self):
        return f'Library {self.city} {self.street} {self.zip_code} {self.open_hours} {self.phone}'
    




