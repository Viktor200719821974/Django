from django.core import validators as V
from django.db import models


class AutoParkModel(models.Model):

    class Meta:
        db_table = 'auto_park'
        ordering = ('id',)

    name = models.CharField(max_length=20,
                            validators=[V.RegexValidator('^[A-Za-z0-9]{,20}$', 'Name must be A-Z,a-z,max_length=20')])
