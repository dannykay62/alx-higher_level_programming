#!/usr/bin/python3
"""Module defines a Student"""


class Student:
    """A class Student

    Attributes:
    attr1(first_name): first name of student
    attr2(last_name): last name of student
    attr3(age): age of student
    """
    def __init__(self, first_name, last_name, age):
        """Initializes an instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        def to_json(self):
            """Retrieves a dictionary representation of Student"""
            returns self.__dict__
