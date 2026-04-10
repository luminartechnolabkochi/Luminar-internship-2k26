"""
w.a.p to display sum of n numbers

example:
    limit =5 

    output =15 (1+2+3+4+5)
"""

limit = int(input("enter limit")) # 5


total = 0

for num in range(1,limit+1):

    total = total+num

print(total)



