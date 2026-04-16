# 


# list comprehension
# [retrun iteration condition]

arr = [ 12,13,14,15,16,17,18,19,20]

odd_list =[num for num in arr if num%2!=0]

even_list= [num for num in arr if num%2==0]

print("odd",odd_list)

print("even",even_list)
