from django.forms import ModelForm
from bookshelf.models import Author, Book
from django.utils.translation import ugettext_lazy as _

__author__ = 'manolo'

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'nickname']
        labels = {
            'name': _("Author's Full Name"),
            'nickname': _("Author's nickname"),
        }
        help_texts = {
            'name': _('The author full name'),
            'nickname': _("Has the author a more popular name? (Optional)")
        }


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'cover', 'synopsis', 'year']
        labels = {
            'title': _("Book title"),
            'author': _("Author of the book"),
            'cover': _("Cover of the book"),
            'synopsis': _("Book synopsis"),
            'year': _("Publication year"),
        }