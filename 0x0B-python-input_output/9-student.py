#!/usr/bin/python3
"""
Contains the clas "Student"
"""


class Student:
     """Representation of a student"""
     def __init__(self, first_name, last_name, age):
     """
     Initializes a Student instanceame, and age.
     """
     self.first_name = first_name
     self.last_name = last_name
     self.age = age

     def to_json(self):
     """
     Retrieves a dictionary representation of a Student instance.
     """
     student_dict = {
             'first_name': self.first_name,
             'last_name': self.last_name,
             'age': self.age
             }
     return student_dict
