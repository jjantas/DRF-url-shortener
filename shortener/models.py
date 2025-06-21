from django.db import models

class ShortURL(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f'{self.original_url} -> http://localhost:8000/shrt/{self.short_code}/'
    