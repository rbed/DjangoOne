from django.db import models

# dodajemy klasy, bo bez klasy nie mozna zdefiniowac obiektu w bazie danych (dla kazdego obiektu klasa)
class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)

# str pozwala na wyswietlanie w panelu admina okreslonych danych obiektu zamiast np "Author obcject""
    def __str__(self):
        return "{first_name} {last_name}" .format(first_name = self.first_name, last_name = self.last_name)


class Publisher(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author)
    isbn = models.CharField(max_length=17)
    publisher = models.ForeignKey(Publisher)

    def __str__(self):
        return self.title