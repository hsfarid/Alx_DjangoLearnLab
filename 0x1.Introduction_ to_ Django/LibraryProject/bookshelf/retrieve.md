#python command
from bookshelf.models import Book
books = Book.objects.all();
print(books);

#expected output
#<QuerySet [<Book: 1984 George Orwell 1949>]>