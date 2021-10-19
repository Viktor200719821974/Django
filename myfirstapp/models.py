from django.db import models

# Create your models here.
class ComputerModel(models.Model):
    class Meta:
        db_table = 'computers'
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    RAM_size = models.IntegerField()
    CPU_frequency = models.IntegerField()
    monitor = models.IntegerField()