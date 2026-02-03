#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
from enum import Enum

# ---------------- CORE LOGIC ---------------- #

class Status(Enum):
    AVAILABLE = "AVAILABLE"
    CHECKED_OUT = "CHECKED_OUT"


class Book:
    def __init__(self, book_id, title, author, status=Status.AVAILABLE):
        self.id = book_id
        self.title = title
        self.author = author
        self.status = status

    def __str__(self):
        return f"{self.id}: {self.title} by {self.author} [{self.status.value}]"


class LibraryCatalog:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        if book.id in self.books:
            raise ValueError("Book ID already exists")
        self.books[book.id] = book

    def list_books(self):
        return list(self.books.values())

    def search(self, title="", author=""):
        return [
            b for b in self.books.values()
            if title.lower() in b.title.lower()
            and author.lower() in b.author.lower()
        ]

    def checkout(self, book_id):
        book = self._get(book_id)
        if book.status == Status.CHECKED_OUT:
            raise ValueError("Already checked out")
        book.status = Status.CHECKED_OUT

    def return_book(self, book_id):
        book = self._get(book_id)
        if book.status == Status.AVAILABLE:
            raise ValueError("Already available")
        book.status = Status.AVAILABLE

    def _get(self, book_id):
        if book_id not in self.books:
            raise ValueError("Book not found")
        return self.books[book_id]


# ---------------- CLI FALLBACK ---------------- #

def run_cli(library):
    while True:
        print("\nLibrary Catalog")
        print("1. List all books")
        print("2. Add book")
        print("3. Search")
        print("4. Check out")
        print("5. Return")
        print("6. Exit")

        choice = input("Choose option: ")

        try:
            if choice == "1":
                for b in library.list_books():
                    print(b)

            elif choice == "2":
                book_id = int(input("ID: "))
                title = input("Title: ")
                author = input("Author: ")
                library.add_book(Book(book_id, title, author))
                print("Book added")

            elif choice == "3":
                title = input("Title (optional): ")
                author = input("Author (optional): ")
                for b in library.search(title, author):
                    print(b)

            elif choice == "4":
                library.checkout(int(input("Book ID: ")))
                print("Checked out")

            elif choice == "5":
                library.return_book(int(input("Book ID: ")))
                print("Returned")

            elif choice == "6":
                break

        except Exception as e:
            print("Error:", e)


# ---------------- GUI ATTEMPT ---------------- #

def run_gui(library):
    import tkinter as tk
    from tkinter import ttk, messagebox

    def execute():
        try:
            action = action_var.get()
            book_id = int(id_entry.get()) if id_entry.get() else None
            title = title_entry.get()
            author = author_entry.get()
            output.delete("1.0", tk.END)

            if action == "List":
                for b in library.list_books():
                    output.insert(tk.END, str(b) + "\n")

            elif action == "Add":
                library.add_book(Book(book_id, title, author))
                messagebox.showinfo("Success", "Book added")

            elif action == "Search":
                for b in library.search(title, author):
                    output.insert(tk.END, str(b) + "\n")

            elif action == "Checkout":
                library.checkout(book_id)
                messagebox.showinfo("Success", "Checked out")

            elif action == "Return":
                library.return_book(book_id)
                messagebox.showinfo("Success", "Returned")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    root = tk.Tk()
    root.title("Library Catalog")

    action_var = tk.StringVar(value="List")
    ttk.Combobox(root, values=["List", "Add", "Search", "Checkout", "Return"],
                 textvariable=action_var, state="readonly").grid(row=0, column=1)

    ttk.Label(root, text="ID").grid(row=1, column=0)
    id_entry = ttk.Entry(root)
    id_entry.grid(row=1, column=1)

    ttk.Label(root, text="Title").grid(row=2, column=0)
    title_entry = ttk.Entry(root)
    title_entry.grid(row=2, column=1)

    ttk.Label(root, text="Author").grid(row=3, column=0)
    author_entry = ttk.Entry(root)
    author_entry.grid(row=3, column=1)

    ttk.Button(root, text="Execute", command=execute).grid(row=4, column=1)
    output = tk.Text(root, width=50, height=10)
    output.grid(row=5, column=0, columnspan=2)

    root.mainloop()


# ---------------- MAIN ---------------- #

library = LibraryCatalog()
library.add_book(Book(1, "1984", "George Orwell"))
library.add_book(Book(2, "The Hobbit", "J.R.R. Tolkien", Status.CHECKED_OUT))

try:
    run_gui(library)
except Exception:
    print("GUI not available — running CLI mode")
    run_cli(library)

