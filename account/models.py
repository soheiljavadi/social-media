from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.
class  Costomuser(AbstractUser):
     username = models.CharField(max_length=150, unique=True)

  