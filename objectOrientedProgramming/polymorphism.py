"""
polymorphism

many forms , more than one form


result = 10 + 20
word = "hello" + "world"

method_over_riding : child class redefines the method that is already defined in parent class
method_over_loading X
"""

class Parent:

    def mobile(self):

        print("parent redmi note 10")

    def vehicle(self):

        print("parent passion pro")

class Child(Parent):

    def mobile(self):

        print("child iphone 17 ")

    def vehicle(self):

        print("child gurilla 450")

child_instance = Child()

child_instance.mobile()

child_instance.vehicle()