"""
parent , child

child class access the methods and attributes of parent class
"""

class Parent:

    def m1(self):

        print("parent class m1 method")



class Child(Parent):

    def m2(self):

        print("child class m2 method")

child_instance = Child()

child_instance.m2()

child_instance.m1()