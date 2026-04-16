"""
number = 123

last_digit = number % 10 123%10=>3

number = number //10 12

last_digit = number % 10 12%10=>2

12=>1.2

number = number //10 1

last_digit = number % 10 =>1

number = number // 10=> 1/10=>0



"""



def reverse_int(number):

    result = ""

    while(number!=0):

        last_digit = number % 10

        result += str(last_digit)

        number = number//10

    print(result)

reverse_int(123)

reverse_int(121)










