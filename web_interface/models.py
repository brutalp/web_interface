# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
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
