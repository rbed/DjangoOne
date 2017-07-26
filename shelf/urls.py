from django.conf.urls import url

from shelf.views import AuthorListView, AuthorDetailView

# w urlpattern najpierw wyrazenie regularne, potem co ma pokazac
# jezel icos nie jest zaimportowane to podkresla na czerowo
urlpatterns = [
    url(r'^authors/$', AuthorListView.as_view(), name='author-list'),
    url(r'^authors/(?P<pk>\d+)/$', AuthorDetailView.as_view(), name='author-detail'),
]