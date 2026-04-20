
class GrandParent:

    def properties(self):

        print("grand parent properties")

class Parent(GrandParent):

    def house(self):

        print("parent house")

class Child(Parent):

    def social_media(self):

        print("scoial media account")

child_instance = Child()

child_instance.social_media()
child_instance.house()
child_instance.properties()