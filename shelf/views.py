from django.shortcuts import render

from django.views.generic import ListView, DetailView # klasy do pokazywania list i szczegolow modelu
# importuje model Author
from .models import Author, Book, Publisher


class AuthorListView(ListView):
    model = Author

class AuthorDetailView(DetailView):
    model = Author

class BookListView(ListView):
    model = Book

class BookDetailView(DetailView):
    model = Book

class PublisherListView(ListView):
    model = Publisher

class PublisherDetailView(DetailView):
    model = Publisher