from django.db import models



class Channel(models.Model):
    title = models.CharField(max_length=100)
    subscriber = models.IntegerField(default=0)
    link = models.URLField()
    keyword = models.CharField(max_length=50)

    def __str__(self):
        return self.title


