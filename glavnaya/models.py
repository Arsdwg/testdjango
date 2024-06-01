from django.db import models

class Motto(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

class YouTubeVideo(models.Model):
    url = models.URLField()

    def __str__(self):
        return self.url

class Gadget(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    popularity = models.PositiveIntegerField()

    def __str__(self):
        return self.name

