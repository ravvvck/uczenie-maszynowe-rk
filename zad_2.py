# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def zad2a_fun(names_list):
  for name in names_list:
      print(name)
      

print("A: \n")
zad2a_fun(['Kasia','Basia', 'Asia','Tomek','Przemek'])


def zad2b_fun(numbers_list):
    
    increased_numbers = []
    for number in numbers_list:
      increased_numbers.append(number*2)
      
    return increased_numbers    
print("B1: \n")
print(zad2b_fun([1,2,3,4,5]))


def zad2b_fun2(numbers_list):
    
    increased_numbers = [number*2 for number in numbers_list]
    return increased_numbers    
print("B2: \n")
print(zad2b_fun2([1,2,3,4,5]))

def zad2c_fun(numbers_list):
    
    for number in numbers_list:
        if number % 2 ==0:
            print(number)
            
        
print("C: \n")
zad2c_fun(range(10))

def zad2d_fun(numbers_list):
    
    for number in numbers_list:
        if (numbers_list[number]+1) % 2 ==0:
            print(number)
        
print("D: \n")
zad2d_fun(range(10))

