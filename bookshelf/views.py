from django.shortcuts import render, get_object_or_404
from .forms import BookForm, AuthorForm
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

def authors_list(request):
    authors = Author.objects.order_by('name')
    return render(request, 'author_list.html', {'authors': authors})

def new_book(request):
    template = 'new_book.html'
    data = {}
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            data['done'] = 'done'
            # do something.
    else:
        form = BookForm()

    data['form'] = form

    return render(request, template, data)


def new_author(request):
    template = 'new_author.html'
    data = {}
    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            data['done'] = 'done'
            # do something.
    else:
        form = AuthorForm

    data['form'] = form

    return render(request, template, data)