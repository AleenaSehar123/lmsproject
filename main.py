# Main library interface
from BookModule import Book
from MemberModule import Member

library_books = [Book("To Kill a Mockingbird", "Harper Lee"),
    Book("1984", "George Orwell"),
    Book("The Great Gatsby", "F. Scott Fitzgerald"),
    Book("Pride and Prejudice", "Jane Austen"),
    Book("The Catcher in the Rye", "J.D. Salinger"),
    Book("The Hobbit", "J.R.R. Tolkien"),
    Book("The Alchemist", "Paulo Coelho"),
    Book("The Lord of the Rings", "J.R.R. Tolkien"),
    Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling"),
    Book("Brave New World", "Aldous Huxley")]
library_members = []
book_id = 1
member_id = 1


def validate_membership(members_list, target_id):
    for member in members_list:
        if member.member_id == target_id:
            return True
    return False 


def get_member_object(members_list, target_id):
    for member in members_list:
        if member.member_id == target_id:
            return member
        

def get_book_object(books_list, target_title):
    for book in books_list:
        if book.title == target_title:
            return book
    return False


print("\nWelcome to Library Management System!")

while True:
    print("\n1. View all books")
    print("2. Add a Book")
    print("3. Register Yourself")
    print("4. Check Out Book")
    print("5. Return Book")
    print("6. Exit\n")

    choice = input("Enter your choice: ")

    if choice == '1':
        print("\n~---~\n")
        for book in library_books:
            print(book.display_book_info())
        print("\n~---~\n")

    elif choice == '2':
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        new_book = Book(title, author)
        library_books.append(new_book)
        print(f"Book '{title}' has been added to the library.")

    elif choice == '3':
        name = input("Enter member name: ")
        new_member = Member(member_id, name)
        library_members.append(new_member)
        print(f"Member '{name}' has been registered with ID {member_id}.")
        member_id += 1

    elif choice == '4':
        member_id = int(input("Enter member ID: "))
        is_a_member = validate_membership(library_members, member_id)
        if is_a_member:
            member_object = get_member_object(library_members, member_id)
            book_title = input("Enter the book title: ")
            book_object = get_book_object(library_books, book_title)
            if book_object:
                member_object.check_out_book(book_object)
                print("Book has been checked out successfully!")
            else:
                print("This book isn't available at the moment!")
        else:
            print("You're not a member. Register yourself first!")
    
    elif choice == '5':
        member_id = int(input("Enter member ID: "))
        member_object = get_member_object(library_members, member_id)
        book_title = input("Enter the book title: ")
        book_object = get_book_object(library_books, book_title)
        if book_object:
            member_object.return_book(book_object)
            print("Book has been returned successfully!")
        else:
            print("This book wasn't issued from this library!")

    elif choice == '6':
        print("Exiting the Library Management System.")
        break

    else:
        print("Invalid choice. Please select a valid option.")
