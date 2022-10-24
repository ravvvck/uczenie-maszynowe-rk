# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 14:00:16 2022

@author: student
"""

import utils

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def is_passed(self):
        if (mean(self.marks) > 50):
            return True
        return False
    
utils.utils_func()

