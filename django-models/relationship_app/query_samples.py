# relationship_app/query_samples.py

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name).objects.filter(name=author_name)
        books = author.books.all()  # Using the related_name 'books'
        return books
    except Author.DoesNotExist:
        return f"Author with name '{author_name}' does not exist."

# List all books in a library
def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()  # Using the related_name 'books'
        return books
    except Library.DoesNotExist:
        return f"Library with name '{library_name}' does not exist."

# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian  # Using the related_name 'librarian'
        return librarian
    except Library.DoesNotExist:
        return f"Library with name '{library_name}' does not exist."
    except Librarian.DoesNotExist:
        return f"No librarian assigned to the library '{library_name}'."

