

# inheritance single,multilevel,multiple
# polymorphism:

class Calculator:


    def operation(self,*args,**kwargs):

        # args=(10,20,30,40)
        #kwargs={"operand":"+"}

        if kwargs.get("operand")=="+":

            print(sum(args))




calc_instance = Calculator()

calc_instance.operation(10,20,30,40,operand="+")
# intership batch assesment program day-wise
# day1 : decision making programs 
# day2 : decision making programs
# day3 :looping programs
# day4 :looping programs
# day5 :list programs
# day6 :list and set programs
# day7 :dictionary programs
# day8 :mixed collection programs along with comprehension
# day9 :oop programs
# day10:oop programs

# front end html,css
# django,mysql