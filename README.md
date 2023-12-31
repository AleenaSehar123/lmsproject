# Documentation

## Overview
This is a simple library management system which allows users to perform various tasks such as viewing all books, adding new books, registering library members, checking out books, and returning books.


## Classes
1. ### Book Class
The `Book` class represents a book in the library. 
#### Each book has the following attributes:
* title (str): The title of the book.
* author (str): The author of the book.
* available (bool): Indicates whether the book is available for checkout.
#### Has the following methods:
* `display_book_info()`: Returns a string with the book's title and author.

2. ### Member Class
The `Member` class represents a library member. 
#### Each member has the following attributes:
* member_id (int): A unique identifier for the member.
* name (str): The name of the member.
* checked_out_books (list): A list of books checked out by the member.
#### Has the following methods:
* `display_member_info()`: Returns a string with the member's ID and name.
* `check_out_book(book)`: Allows a member to check out a book. It updates the book's availability and adds it to the member's list of checked-out books.
* `return_book(book)`: Allows a member to return a checked-out book. It updates the book's availability and removes it from the member's list of checked-out books.

## Features and Functionality
* View all books: Displays information about all the books in the library.
* Add a Book: Allows users to add a new book to the library.
* Register Yourself: Allows users to register themselves as library members.
* Check Out Book: Enables registered members to check out a book.
* Return Book: Enables registered members to return a checked-out book.
* Exit: Allows users to exit the program.
<br>
The program ensures input validation and provides appropriate feedback to users.

# Process
1. ## Created a GitHub repository
For a start, we created a GitHub repository which would eventually contain all the source code and documentation for this project.

2. ## Created a branch `Feature` and made the initial commit
One of us (the team member who had initially created the repository), cloned the repository on her local machine, 
switched into a new `Feature` branch, added code for classes `Book` and `Member`, pushed the changes into the `Feature` branch, merged the changes into the `main branch`, and pushed them to the repository.

3. ## Forked the repository
The other team member forked the repository:
<br>
<img width="684" alt="Screenshot 2023-10-21 203147" src="https://github.com/ayeshag7/Chat2PDF/assets/106478752/55d715f1-a617-49cf-9b4a-7fb6fbafeb12">
<br>
And then cloned the forked repository onto her local machine:
<br>
<img width="549" alt="Screenshot 2023-10-21 203314" src="https://github.com/ayeshag7/Chat2PDF/assets/106478752/6e7df3b8-baec-4d94-8a1e-e727aa3b1877">
<br>

4. ## Created a branch `Functionality` and made the second commit
That team member after forking and cloning the repository successfully, switched to a new branch `Functionality`, added the code for the main functionality, pushed the changes onto the `Functionality` branch, merged it into the `main` branch, and then opened a pull request to be merged into the original main branch of the repository:
<br>
<img width="691" alt="Screenshot 2023-10-21 191122" src="https://github.com/ayeshag7/Chat2PDF/assets/106478752/c79fc818-1c80-4fc8-b347-065eb87de594">
<br>

5. ## Merged the pull request
The first team member who had initially created the repository merged the pull request into the original main branch successfully:
<br>
![WhatsApp Image 2023-10-21 at 7 19 07 PM](https://github.com/ayeshag7/Chat2PDF/assets/106478752/d5e35692-a5d7-42ea-a326-7638affdad95)
<br>

