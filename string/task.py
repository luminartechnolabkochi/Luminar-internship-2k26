#            0987654321  -
word="pythonprogramming"
#     01234567890123456
#               1

# q1 print first 6 characters

first_six_char=word[0:6]

print(first_six_char)

# q2 last 5 characters

last_five = word[-5:]

print(last_five)

# q3 characters from index 3 to 10
three_to_ten = word[3:11]

# q4 split word in to two equal part left and right

word_length = len(word)-1 #16

mid = word_length//2 #8

left=word[:mid]

right=word[mid:]

print(left)

print(right)
