from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book
from .models import Library

# Create your views here.
#function that list all books stored in the database
def list_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)

#CBV that displays details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'libary'