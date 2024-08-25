from relationship_app.models import Author, Book, Library, Liberian

#query all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = author.books.all()  # Using the related_name 'books' from the ForeignKey
        return books
    except Author.DoesNotExist:
        return []

# Query 2: List all books in a library
def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()  # Using the related_name 'libraries' from the ManyToManyField
        return books
    except Library.DoesNotExist:
        return []

# Query 3: Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian  # Using the related_name 'librarian' from the OneToOneField
        return librarian
    except Library.DoesNotExist:
        return None