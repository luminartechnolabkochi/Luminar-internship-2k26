# Book>title,author,price,pages

class Book:

    def __init__(self,title,author,price,pages):

        self.title = title

        self.author = author

        self.price = price

        self.pages = pages

    def display_book(self):

        print(self.title,self.author,self.price,self.pages)

# constructor => initialize attributes of a class
# java => same as class name
# constructor()=>js
# __init__()=>py
# 

book_instance1 = Book("randamoozham","mt",1400,560)


book_instance2=Book()


book_instance1.__init__("randamoozham","mt",550,670)

book_instance1.display_book()

