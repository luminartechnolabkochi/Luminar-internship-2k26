

class Bank:

    def __init__(self,acno,customer_name,ac_type):

        self.acno = acno

        self.customer_name = customer_name

        self.ac_type = ac_type

        self.balance = 2000

    def deposit(self,amount):

        self.balance+=amount

        print("your accout credited with",amount,"bal",self.balance)

    def withdraw(self,amount):

        self.balance-=amount
        print("your accout debited with",amount,"bal",self.balance)

    def get_balance(self):

        print("your avl bal is",self.balance)

bank_instance =Bank(1124,"vijin","savings")

bank_instance.deposit(5000)


    