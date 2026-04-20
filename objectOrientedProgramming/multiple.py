

class Father:

    def cricket_skill(self):

        print("parent cricket skill")


class Mother:

    def cooking_skill(self):

        print("mother cooking skill")


class Son(Father,Mother):

    def coding_skill(self):

        print("son coding skill")

son_instance = Son()

son_instance.coding_skill()
son_instance.cooking_skill()
son_instance.cricket_skill()

