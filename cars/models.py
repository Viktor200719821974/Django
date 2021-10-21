from django.db import models
from django.core import validators as V

from auto_park.models import AutoParkModel

# Create your models here.
class CarModel(models.Model):
    class Meta:
        db_table = 'cars'
    brand = models.CharField(max_length=20,
                             validators=[V.RegexValidator('^[A-Z0-9]{,20}$','Brand must be A-Z, 0-9, max-length=20')])
    model = models.CharField(max_length=20,
                             validators=[V.RegexValidator('^[a-zA-Z0-9]{,20}$','Model must be A-Z, a-z, 0-9, '
                                                                               'max-length=20')])
    color = models.CharField(max_length=20,
                             validators=[V.RegexValidator('^[a-z]{,20}$','Color must be a-z,max-length=20')])
    year = models.IntegerField(validators=[V.MinValueValidator(1990), V.MaxValueValidator(2021)])
    autoPark = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars')