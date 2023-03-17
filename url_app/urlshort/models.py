from django.db import models

class ShortURL(models.Model):
    original_url = models.URLField(max_length=250)
    short_url = models.CharField(max_length=100)
    time_date_created = models.DateTimeField()

    def __str__(self):
        return self.original_url
