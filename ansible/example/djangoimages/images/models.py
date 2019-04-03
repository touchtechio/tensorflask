import datetime


from django.db import models
from django.utils import timezone


from taggit.managers import TaggableManager


# Create your models here.
class Image(models.Model):
    filename = models.CharField(max_length=100)
    extension = models.CharField(max_length=10)
    directory = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    tags = TaggableManager()

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.filename


class Region(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    type = models.CharField(max_length=200)
    top = models.IntegerField(default=0)
    left = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    trainable = models.BinaryField(default=False)

    def __str__(self):
        return '{[' + str(self.top) \
               + ', ' + str(self.left) \
               + '], [' + str(self.height) \
               + ', ' + str(self.width) + ']}'

