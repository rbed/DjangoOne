from django.shortcuts import render

from django.views.generic import ListView, DetailView # klasy do pokazywania list i szczegolow modelu

# importuje model Author
from .models import Author

class AuthorListView(ListView):
    model = Author

class AuthorDetailView(DetailView):
    model = Author
