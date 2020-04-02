from django.db import models

# Create your models here.


class contactRequest(models.Model):

    name = models.CharField(max_length=128, verbose_name="")
    email = models.EmailField(max_length=254)
