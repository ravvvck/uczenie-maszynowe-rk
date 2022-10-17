# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 14:00:32 2022

@author: student
"""

#zad2

class Library:
    def __init__(self, city, street, zip_code, open_hours,phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone
     
    def __str__(self):
        return f'Library {self.city} {self.street} {self.zip_code} {self.open_hours} {self.phone}'
    


class Employee:
    def __init__(self,first_name, last_name, hire_date, birth_date, city, street, zip_code,  phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone
        
    def __str__(self):
        return f'Employee: {self.first_name} {self.last_name} {self.hire_date} {self.birth_date} {self.city} {self.street} {self.zip_code} {self.phone}  '


class Book:
    def __init__(self,library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages
        
    def __str__(self):
        return f'Book: Books Library:{self.library} \n {self.publication_date} {self.author_name} {self.author_surname} {self.number_of_pages}'
class Order:
    
    def __init__(self,employee, student, books:list, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date
        
    def __str__(self):
        books = []
        for book in self.books:
            books.append(str(book))
        books = ' '.join(books)
        return f'Book: {self.employee} {self.student} {books} {self.order_date}'


Library1 = Library('katowice','Bogucicka 6','40-282', '8-18','123-123-123')
Library2 = Library('kielce','Wojewdzka 26','25-002', '8-18','542-128-123')

print(Library1)
Employee1 = Employee("Jan","Kowalski","12-05-2022", "01-01-2000", "Katowice", "Bogucicka 7", "40-282", "123-123-123")
Employee2 = Employee("Piotr","Patuszak","12-05-2022", "01-01-2001", "Katowice", "3 Maja 17", "40-282", "123-123-123")        
Employee3 = Employee("Michał","Patuszak","12-05-2022", "01-01-1996", "Katowice", "Wojewdzka 15/7", "40-282", "123-123-123")        

Book1 = Book(Library1, '12-12-1966', 'Jan','Kowalski', 666)
Book2 = Book(Library1, '12-12-19662', 'Jan2','Kowalski2', 666)
Book3 = Book(Library1, '12-12-19663', 'Jan3','Kowalski3', 666)
Book4 = Book(Library2, '12-12-19664', 'Jan4','Kowalski4', 666)
Book5 = Book(Library2, '12-12-19665', 'Jan5','Kowalski5', 666)

Order1 = Order(Employee1, 'student1', [Book1,Book2], '12-12-2022')
Order2 = Order(Employee2, 'student2', [Book3,Book4], '13-12-2022')

print(Order1)