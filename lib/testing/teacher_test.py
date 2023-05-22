#!/usr/bin/env python3

from teacher import Teacher
from user import User

my_teacher = Teacher("My", "Teacher")

class TestTeacher:
    '''Class "Teacher" in teacher.py'''

    def test_is_subclass(self):
        '''is a subclass of "User".'''
        assert(User in Teacher.__bases__)

    def test_initializes_with_names(self):
        '''initializes with first and last name.'''
        assert((my_teacher.first_name, my_teacher.last_name) == ("My", "Teacher"))

    def test_has_attribute_knowledge(self):
        '''has an attribute called "knowledge", a list with len > 0.'''
        assert(isinstance(my_teacher.knowledge, list) and len(my_teacher.knowledge) > 0)

    def test_can_teach(self):
        '''teaches from list of knowledge.'''
        my_teacher.teach(["Python", "Math", "History"])
        assert(all(topic in my_teacher.knowledge for topic in ["Python", "Math", "History"]))
