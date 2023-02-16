from django.db import models


class User(models.Model):
    name = models.CharField(max_length=64, null=True)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=40)
    age = models.IntegerField()
    gender = models.BooleanField()

    def __str__(self):
        result = f' {self.name}, {self.email}, {self.age}, {self.gender}'
        return result