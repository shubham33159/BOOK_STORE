from django.shortcuts import get_object_or_404, render
from book_outlet.models import Book
from django.http import Http404
from django.db.models import Avg

# Create your views here.

def index(request):
    books = Book.objects.all().order_by("-title")
    books_count = books.count()
    avg_books = books.aggregate(Avg("rating"))

    return render(request, "book_outlet/index.html", {
        "books": books,
        "books_count": books_count,
        "avg_books" : avg_books
    })

def book_detail(request, slug):
    # try:
    #     book = Book.objects.get(pk=id)
    # except:
    #     return Http404

    book = get_object_or_404(Book, slug=slug)
    return render(request, "book_outlet/book_detail.html", {
        "title" : book.title,
        "author" : book.author,
        "rating": book.rating,
        "is_bestseller" : book.is_bestselling
    })