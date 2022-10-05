"""
Abstraction :-
----------------
    The Abstraction is used to hide the internal functionality of the function from the users. The user only interacts
with the basic implementation of the function, but inner working is hidden from the user. The user is familiar with
"what function does" but they don't know "How it does".

    For Example, We all use smartphones and very much familiar with it's functions such as camera, voice-recorder, etc.,
but we don't know how these operations are happening in the background. This is exactly the abstraction that works in
the OOP concept

Why Abstraction is important :-
---------------------------------
    In Python, an abstraction is used to hide the irrelevant data/class in order to reduce the complexity. It also
enhances the application efficiency.

"""
from abc import abstractmethod


class Library:
    @abstractmethod
    def __init__(self, books):
        self.books = books

    def display_books(self):
        count = 0
        for book in self.books:
            count += 1
            print(f'({count}) {book}')

    def borrow_books(self, book):
        if book in self.books:
            print("Your Book is Available Sir/Madam. Get the required book")
            self.books.remove(book)
        else:
            print("Sorry Book not available. We'll let you know once the book is available in the library")

    def return_books(self, book):
        if book in self.books:
            print("The Book is already present in the library. No need to return it. Keep it yourself")
        else:
            self.books.append(book)
            print(f"Thank you for returning the '{book}' book sir.")


no_of_books = int(input("Enter the no of books te be present in the library : "))
books = []
for book in range(1, no_of_books + 1):
    individual_book = input(f"Enter the name of the Book {book} : ")
    books.append(individual_book)

library = Library(books=books)
while True:
    print(
        """
        Enter '1' to Display the book
        Enter '2' to Borrow the book
        Enter '3' to Returning the book 
        Enter '4' to Quit
        """
    )

    choice = int(input("Enter your choice : "))
    if choice == 1:
        library.display_books()
    elif choice == 2:

        library.borrow_books(input("Enter the book you want to borrow from the list : "))
    elif choice == 3:
        library.return_books(input("Enter the book that you want to return : "))
    else:
        break
