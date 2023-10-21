# Code for 'BookModule':
class Book:
    def _init_(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

    def display_book_info(self):
        return f"{self.title} by {self.author}"