"""
overloading:with in calss same method name different number of parameter

"""

class Calculator:

    def add(self,n1,n2):

        print(n1+n2)

    def add(self,n1,n2,n3):

        print(n1+n2+n3)

    def add(self,n1,n2,n3,n4):

        print(n1+n2+n3+n4)

calc_instance = Calculator()

calc_instance.add(10,20,30,40) #100

calc_instance.add(10,20,30)

