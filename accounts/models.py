from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
class URL(models.Model):
    long_url=models.URLField(unique=True)
    short_code=models.CharField(max_length=10,unique=True)

    def __str__(self):
        return f"{self.long_url} -> {self.short_code}"