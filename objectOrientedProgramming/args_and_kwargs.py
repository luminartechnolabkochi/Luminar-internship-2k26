

class Calculator:


    def add(self,*args):

        print(sum(args))


calc_instance = Calculator()

calc_instance.add(10,20)
calc_instance.add(10,20,30)
calc_instance.add(10,20,30,40)