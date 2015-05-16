from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^book/(?P<book_id>[0-9]+)/$', views.book_detail, name='book_detail'),
    url(r'^author/(?P<author_id>[0-9]+)/$', views.author_detail, name='author_detail'),

]
