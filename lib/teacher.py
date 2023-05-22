#!/usr/bin/env python

from user import User

import random

class Teacher(User):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.knowledge = ["Python", "Math", "History"]
    def teach(self, knowledge_list):
        self.knowledge.extend(knowledge_list)