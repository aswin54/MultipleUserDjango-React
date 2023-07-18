from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework.authtoken.models import Token


# Create your models here.
class User(AbstractUser):
    is_customer = models.BooleanField(default=False)

    def __str__(self):
        return self.username


@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    contact_no = models.CharField(max_length=25)
    address = models.TextField()

    def __str__(self):
        return self.user.username
