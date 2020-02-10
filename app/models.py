from django.db import models

# Create your models here.
class contactRequest(models.Model):

    name = models.CharField(max_length=128,verbose_name="")
    email = models.EmailField(max_length=254)
    PLANS = (
    (100, '100SAR'),
    (200, '200SAR'),
    (300, '300SAR'),
    )
    plan = models.IntegerField(default=2, choices=PLANS,verbose_name="Plan")