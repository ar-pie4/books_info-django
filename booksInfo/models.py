from django.db import models

# Create your models here.
class Books(models.Model):
    book_name = models.CharField(max_length=10)
    author_name = models.CharField(max_length=20)
    book_price = models.IntegerField()
    book_quantity = models.IntegerField()


    def __str__(self):
        return self.book_name