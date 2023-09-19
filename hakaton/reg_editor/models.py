from django.db import models

class User(models.Model):
    name = models.AutoField(primary_key=True)
    surname = models.CharField(max_length=255)
    birthday = models.CharField(max_length=255)

    def __str__(self):
        return self.name