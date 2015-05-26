from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^book/(?P<book_id>[0-9]+)/$', views.book_detail, name='book_detail'),
    url(r'^author/(?P<author_id>[0-9]+)/$', views.author_detail, name='author_detail'),
    url(r'^authors/$', views.authors_list, name='authors_list'),
    url(r'^book/new/$', views.new_book, name='new_book'),
    url(r'^author/new/$', views.new_author, name='new_author'),
]
