from django.db import models

# Create your models here.
class Card(models.Model):
    index_no = models.CharField(max_length=10)
    content = models.TextField()
    said_by = models.CharField(max_length=50)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.content

class EmailStore(models.Model):
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.email

