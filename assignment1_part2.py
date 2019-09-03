class Book(object):
    author = ""
    title = ""
    
    def __init__(self, author, title):
        self.author = author
        self.title = title

    def display(self):
        print("{0}, written by {1}".format(self.title, self.author))

book1 = Book("John Steinbeck", "Of Mice and Men")
book2 = Book("Harper Lee", "To Kill a Mockingbird")

book1.display()
book2.display()