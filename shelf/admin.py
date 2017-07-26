from django.contrib import admin

# I - z modeli importujemy obiekty jakie stworzylismy
from .models import Author, Publisher, Book

# I - dodajemy obiekty do admina (pole zlikwidowane poniewaz wszystkie klasy zarejestrowalismy osobno w kolejnych krokach, wszystko opisane ponizej)


# II - udoskonalanie panelu admina
# 1 - dodajemy klase dziedziczaca z tego co w nawiasie
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['last_name', 'first_name'] # dodaje wyszukiwarke do admina authorow
    ordering = ['last_name'] # dodaje sortowanie po nazwisku do admina authorow
# 2 rejestrujemy klase zeby dzialala (zwroc uwage, ze inna skladnia, bez []) najpierw model - Author, potem klasa AuthorAdmin
# uwaga, pierwotnie w I byl zarejestrowany ([Author, Publisher, Book]), ale nie mozna 2x zarejestrowac tego samego modelu, wiec
# zostalo to zmienione na ([Publisher, Book]), zeby w rejestracji klasy AuthorAdmin mozna bylo dac (Author, AuthorAdmin)
# potem zaczelismy dodawac inne klasy co spowodowalo zupelne rozjebanie rejestracji o ktorej pisze wyzej
admin.site.register(Author, AuthorAdmin)


# III -
# 1- robimy klase BookAdmin
class BookAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'author', 'isbn', 'publisher']
# 2- rejestrujemy klase
admin.site.register(Book, BookAdmin)


# IV -
# 1 robimy klase PublisherAdmin
class PublisherAdmin(admin.ModelAdmin):
    pass
# 2 - rejestrujemy klase
admin.site.register(Publisher, PublisherAdmin)