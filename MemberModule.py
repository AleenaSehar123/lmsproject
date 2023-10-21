# Code for 'MemberModule':
from BookModule import Book


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.checked_out_books = []

    def display_member_info(self):
        return f"Member ID: {self.member_id}\nName: {self.name}"

    def check_out_book(self, book):
        try:
            if isinstance(book, Book):  # Check if book is an instance of the Book class
                if book.available:
                    book.available = False
                    self.checked_out_books.append(book)
                    return f"{self.name} has checked out {book.title}."
                else:
                    return f"{book.title} is not available for checkout."
            else:
                return "Invalid book object. Please provide a valid Book object."
        except Exception as e:
            return f"An error occurred: {str(e)}."

    
    def return_book(self, book):
        try:
            if isinstance(book, Book):   # Check if book is an instance of the Book class
                if book in self.checked_out_books:
                    book.available = True
                    self.checked_out_books.remove(book)
                    return f"Thank you, {self.name}, for returning {book.title}."
                else:
                    return f"{self.name} did not check out {book.title}."
            else:
                return "Invalid book object. Please provide a valid Book object."
        except Exception as e:
            return f"An error occurred: {str(e)}"