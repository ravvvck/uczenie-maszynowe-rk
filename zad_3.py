# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 14:35:31 2022

@author: student
"""

#1

def zad1(name: str , surname: str ):
    return "czesc "+name + " " + surname

result = zad1("Jan","Kowalski")
print(result)

#2
def zad2(x:int, y:int):
    return x*y

#3

def zad3(x:int):
    if (x % 2 ==0):
        return True
    return False


print(zad3(1))

#4

def zad4(x:int,y:int,z:int):
    if ((x+y)>=z):
        return True
    return False

print(zad4(1,2,4))

#5

def zad5(l:list, n:int):
    if (n in l):
        return True
    return False

print(zad5([1,2,3],4))

#6

def zad6(l1:list,l2:list):
    l_joined = list(set(l1 + l2))
    l_joined= [x**3 for x in l_joined]
    
    return l_joined

print(zad6([1,2,3], [3,5,6]))