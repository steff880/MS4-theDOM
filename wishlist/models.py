from django.db import models
from django.contrib.auth.models import User
from courses.models import Course


class WishList(models.Model):
    """
    Model to show all courses in the users wishlist
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    courses = models.ManyToManyField(
        Course, through="WishListItem", related_name='course_wishlists')

    def __str__(self):
        return f'WishList ({self.user})'


class WishListItem(models.Model):
    """
    A 'through' model, allowing users to add
    individual courses to their wishlist.
    """

    course = models.ForeignKey(
        Course, null=False, blank=False, on_delete=models.CASCADE)
    wishlist = models.ForeignKey(
        WishList, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.course.name
