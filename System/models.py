from django.db import models


class Library(models.Model):
    book_id= models.IntegerField(primary_key=True, unique=True)
    book_name = models.CharField(max_length=100)
    book_author = models.CharField(max_length=100)
    date_of_publish = models.DateField()
    book_price = models.IntegerField()

    def __str__(self):
        return self.book_name

