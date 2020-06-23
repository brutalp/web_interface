from django.db import models


class Measurmement(models.Model):
    datatime_d = models.DateField(blank=True, null=True)
    datatime_h = models.TimeField(blank=True, null=True)
    obrazec = models.CharField(max_length=30, blank=True, null=True)
    sera = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    rasseyanoe = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    koncentracia = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    analprog = models.CharField(max_length=30, blank=True, null=True)
    operator = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'measurmement'
