from django.db import models
from django.core import validators as V

# Create your models here.
class AirPlaneModel(models.Model):
    class Meta:
        db_table = 'airplane'

    designation = models.CharField(max_length=20,
                                   validators=[V.RegexValidator('^[a-zA-Z0-9]{,20}$', 'Name must be only a-z, A-Z, 0-9, '
                                                                                      'max = 20')])
    name = models.CharField(max_length=20,
                            validators=[V.RegexValidator('^[a-zA-Z0-9]{,20}$',  'Name must be only a-z, A-Z, 0-9,'
                                                                                ' max = 20')])
    speed = models.IntegerField(validators=[V.MinValueValidator(200), V.MaxValueValidator(1000)])
    engine = models.FloatField(validators=[V.MinValueValidator(10), V.MaxValueValidator(20)])
    weight = models.FloatField(validators=[V.MinValueValidator(20), V.MaxValueValidator(500)])
    year  = models.IntegerField(validators=[V.MinValueValidator(1980), V.MaxValueValidator(2021)])