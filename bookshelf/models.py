from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    def get_nickname(self):
        if self.nickname == '':
            return self.name.split(" ")[0]

        return self.nickname


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author)
    synopsis = models.TextField(blank=True)
    year = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.title