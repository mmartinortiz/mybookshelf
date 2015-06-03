# from django.forms import ModelForm, ImageField
from bookshelf.models import Author, Book
from django import forms
from django.utils.translation import ugettext_lazy as _
# from widgets import ImageWidget
from widgets import ImageWidget

__author__ = 'manolo'

class AuthorForm(forms.ModelForm):
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


class BookForm(forms.Form):
    cover = forms.ImageField(widget=ImageWidget(width=200, height=300))

    # class Meta:
    #     model = Book
    #     fields = ['title', 'author', 'synopsis', 'year']
    #
    #     labels = {
    #         'title': _("Book title"),
    #         'author': _("Author of the book"),
    #         'cover': _("Cover of the book"),
    #         'synopsis': _("Book synopsis"),
    #         'year': _("Publication year"),
    #     }