
# n=5
# 5!= 1*2*3*4*5

def factorial(number):
    result = 1
    for i in range(1,number+1):

        result=result*i

    print(result)

factorial(5)
factorial(6)
factorial(7)

