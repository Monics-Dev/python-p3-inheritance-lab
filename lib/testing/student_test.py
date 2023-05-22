#!/usr/bin/env python3

from teacher import Teacher  # Assuming the Teacher class is imported from teacher.py
from student import Student
from user import User
        
class TestStudent:
    '''Class "Student" in student.py'''

    def test_is_subclass(self):
        '''is a subclass of "User".'''
        assert(User in Student.__bases__)

    def test_initializes_with_names(self):
        '''initializes with first and last name.'''
        my_student = Student("My", "Student")
        assert((my_student.first_name, my_student.last_name) == ("My", "Student"))

    def test_initializes_with_knowledge(self):
        '''initializes with empty list attribute "knowledge".'''
        my_student = Student("My", "Student")
        assert(hasattr(my_student, "knowledge"))

    def test_can_learn(self):
        '''learns from a string and adds to self.knowledge.'''
        my_student = Student("My", "Student")
        my_student.learn("New information")
        assert("New information" in my_student.knowledge)


class TestTeacher:
    '''Class "Teacher" in teacher.py'''

    def test_initializes_with_names(self):
        '''initializes with first and last name.'''
        my_teacher = Teacher("John", "Doe")
        assert((my_teacher.first_name, my_teacher.last_name) == ("John", "Doe"))

    def test_has_knowledge_attribute(self):
        '''has an attribute called "knowledge", a list with len > 0.'''
        my_teacher = Teacher("John", "Doe")
        assert(hasattr(my_teacher, "knowledge") and len(my_teacher.knowledge) > 0)

    def test_can_teach(self):
        '''teaches from a list of knowledge.'''
        my_teacher = Teacher("John", "Doe")
        my_teacher.teach(["Python", "Math", "History"])
        assert(all(topic in my_teacher.knowledge for topic in ["Python", "Math", "History"]))
