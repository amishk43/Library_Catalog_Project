# Library_Catalog_Project

## Overview
Users can manage a collection of books with this project's straightforward Library Catalog application. While upholding fundamental library policies (such prohibiting a book from being checked out twice), it facilitates the addition, viewing, searching, checking out, and returning of books. Instead of creating a production-scale system, the objective of this project is to illustrate fundamental software development ideas including data modeling, rule enforcement, clean code structure, and usability.

## Features
The features that are included in this project allow the users:
1. Add new books
2. View all books
3. Search for books by title or author
4. Search for books by availability
5. Check out books
6. Return books

## Tech Stack
For this project I used Python code and the built in Python GUI library, Tkinter, no other libraries or databases are needed.

## How to run locally
In order to run the code you must have Python 3.9 or newer and a local destop enviornment for the Tkinter GUI.
1. Download the repository
2. Open a terminal
3. Navigate to the folder with "cd/path/to/project"
4. Run the code with "python Library_Catalog.py"
If all goes well then a GUI enviornment will become available and a window with a dropdown and menu will appear.

## Mock Data
For ease of use, mock book data is immediately hardcoded into the program. A number of example books are automatically added to the catalog when the application launches. This makes it possible to display the program right away without the need for external files or manual setup.

## Assumptions and Tradeoffs
1. The catalog uses in-memory storage, so data resets each time the program is restarted.
2. No database is used to keep the project easy to run locally.
3. The GUI is intentionally simple to focus on functionality and rule enforcement.
4. Inventory count and borrower tracking are not implemented to keep the scope manageable.
In a production system, these tradeoffs would be addressed using persistent storage and additional validation.

## Use of AI Tools
ChatGPT was used to:
Assist with Tkinter syntax
review logic for rule enforcement and overall code stability

