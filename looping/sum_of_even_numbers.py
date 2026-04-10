

"""
w.a.p to display sum of even number upto limit
"""

limit = int(input("enter limit"))

total = 0

for num in range(1,limit+1):

    if num%2==0:

        total= total+ num

print(total)

