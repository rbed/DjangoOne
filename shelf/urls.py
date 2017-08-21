from django.conf.urls import url

from shelf.views import AuthorListView, AuthorDetailView, BookListView, BookDetailView, PublisherListView, PublisherDetailView

# w urlpattern najpierw wyrazenie regularne, potem co ma pokazac
# jezel icos nie jest zaimportowane to podkresla na czerowo
urlpatterns = [
    url(r'^authors/$', AuthorListView.as_view(), name='author-list'),
    url(r'^authors/(?P<pk>\d+)/$', AuthorDetailView.as_view(), name='author-detail'),
    url(r'^books/$', BookListView.as_view(), name='book-list'),
    url(r'^books/(?P<pk>\d+)/$', BookDetailView.as_view(), name='book-detail'),
    url(r'^publishers/$', PublisherListView.as_view(), name='publisher-list'),
    url(r'^publishers/(?P<pk>\d+)/$', PublisherDetailView.as_view(), name='publisher-detail'),
]