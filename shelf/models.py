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


class BookCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    cos w rodzaju rekopisu
    """
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    categories = models.ManyToManyField(BookCategory)
    # author = models.ForeignKey(Author)

    def __str__(self):
        return self.title

class BookEdition(models.Model):
    """
    wydanie
    """
    book = models.ForeignKey(Book)
    publisher = models.ForeignKey(Publisher)
    date = models.DateField()
    isbn = models.CharField(max_length=17, blank=True)

    def __str__(self):
        return "{book.title}, {publisher.name}".format(book=self.book, publisher=self.publisher)



class BookItem(models.Model):
    """
    egzemnplarz
    """
    edition = models.ForeignKey(BookEdition)
    catalogue_numb = models.CharField(max_length=30)
#    cover_type = models.CharField(max_length=4, choices=COVER_TYPES)
    hard = 'Hard'
    soft = 'Soft'
    COVER_TYPES = (
        ('soft', 'Soft'),
        ('hard', 'Hard'),
        # wartosc w bazie, wartosc wysywietlana
    )

    cover_type = models.CharField(
        max_length=4,
        choices=COVER_TYPES,
        default=soft,
    )

    def __str__(self):
        return "{edition}, {cover}, {number}".format(edition=self.edition,
                                                     #cover=self._get_FIELD_display(self.cover_type),
                                                     cover=self.cover_type in (self.soft, self.hard),
                                                     number=self.catalogue_numb)


#16:40
#odc 5 (55:00) - omawia korzystanie z shella - WAZNE