


class Employee:

    def __init__(self,**kwargs):
        # kwargs={"name":"jibin","department":"hr","salary":15000}

        print(kwargs)




emp_instance = Employee(name="jibin",department="hr",salary="15000",location="kakknad",native="thrissur")