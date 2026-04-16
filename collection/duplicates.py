lst =[10,11,11,10,13,15,11]

duplicates = []





















for num in lst:

    freq = lst.count(num)

    if freq>1 and num not in duplicates:

        duplicates.append(num)

print(duplicates)

# collection  define          
# list          []  duplicates allowed  ordered mutable 

# tuple

# set

# dictionary