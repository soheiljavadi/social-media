from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.
class  Costomuser(AbstractUser):
  
    first_name=models.CharField(_('first_name'),max_length=30,unique=True)

    last_name=models.CharField(max_length=10)

    email=models.EmailField()

    is_active = models.BooleanField(
        _("active_user"),
        default=True,
       )
    
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_(
            "Designates whether the user can log into this admin site."))
