from django.db import models
from embed_video.fields import EmbedVideoField


class Category(models.Model):
    """ Category model """

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, blank=True)

    def __str__(self):
        """ Return name """
        return self.name

    def get_friendly_name(self):
        """ Return friendly name """
        return self.friendly_name


# How to embed video:
# https://www.youtube.com/watch?v=-AOPAqxAFJk&list=LL&index=3
class Course(models.Model):
    """ Course model """
    category = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    video = EmbedVideoField()

    def __str__(self):
        return self.name
