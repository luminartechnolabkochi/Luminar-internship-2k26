
"""
class list:
    def append(object) add object at end of the list
    def insert(index,element) add element at specified index
    def pop(index=-1) remove element at specified index
    def remove(value) remove value from list
    def reverse()
    def index(value,start) => retrun index of  first occurance value
    
"""

favt_colors = ["red","green","blue","yellow","green"]
#                0     1       2      3         4

# pos=favt_colors.index("green")


last_pos=favt_colors.index("green",2)

print(last_pos)

# favt_colors.reverse()

# print(favt_colors)

# favt_colors.remove("green")

# print(favt_colors)

# print(favt_colors.pop(1))# green

# print(favt_colors)#red,blue,yellow

