class Author: 
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def publish(self, title):
        if title in self.books:
            print('This book has already been published')
        else:
            self.books.append(title)

    def __str__(self):
        titles = ', '.join(self.books) or 'No books published'
        return (self.name) + ': ' + (titles)
    
a1 = Author('Suzanne Collins')
a1.publish('The Hunger Games')
a1.publish('Catching Fire')
a1.publish('The Hunger Games')
a2 = Author('Stephen King')
a2.publish('IT')
print(a1)
print(a2)













