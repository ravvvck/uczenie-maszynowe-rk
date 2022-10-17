# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 13:47:38 2022

@author: student
"""

#zad1
from statistics import mean

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def is_passed(self):
        if (mean(self.marks) > 50):
            return True
        return False
    
student_1 = Student("Piotr", [1,2,3] ) 
print(student_1.is_passed())

student_2 = Student("Michał", [51,52,53] ) 
print(student_2.name,student_2.is_passed())