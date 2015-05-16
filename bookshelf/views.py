from django.shortcuts import render, get_object_or_404
from .models import Book, Author


# Create your views here.
def index(request):
    books = Book.objects.order_by('title')
    return render(request, 'index.html', {'books': books})


def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'book_details.html', {'book': book})


def author_detail(request, author_id):
    # Get the author
    author = get_object_or_404(Author, pk=author_id)

    # Get all the author's books
    books = author.book_set.all()
    return render(request, 'author_details.html', {'author': author, 'books': books})