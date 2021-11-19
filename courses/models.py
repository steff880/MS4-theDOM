from django.db import models
from django.contrib.auth.models import User
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


class CourseReview(models.Model):
    """
    Course Review Model
    """

    class Meta:
        ordering = ['-date_added']

    rating_selection = (
        (5, '5'),
        (4, '4'),
        (3, '3'),
        (2, '2'),
        (1, '1'),
    )

    course = models.ForeignKey(
        Course,
        related_name='reviews', null=True, blank=True,
        on_delete=models.SET_NULL)
    user = models.ForeignKey(User,
                             null=True,
                             blank=True,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=254)
    content = models.TextField()
    rating = models.IntegerField(choices=rating_selection, default=3)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
