# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    experimentos = models.IntegerField(null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Experimentos(models.Model):

    #__Experimentos_FIELDS__
    nombre = models.CharField(max_length=255, null=True, blank=True)
    fecha = models.DateTimeField(blank=True, null=True, default=timezone.now)
    descripcion = models.TextField(max_length=255, null=True, blank=True)

    #__Experimentos_FIELDS__END

    class Meta:
        verbose_name        = _("Experimentos")
        verbose_name_plural = _("Experimentos")


class Pozos(models.Model):

    #__Pozos_FIELDS__
    numero = models.IntegerField(null=True, blank=True)
    operativo = models.BooleanField()
    experimento = models.ForeignKey(experimentos, on_delete=models.CASCADE)

    #__Pozos_FIELDS__END

    class Meta:
        verbose_name        = _("Pozos")
        verbose_name_plural = _("Pozos")


class Datos_Pozos(models.Model):

    #__Datos_Pozos_FIELDS__
    numero = models.IntegerField(null=True, blank=True)
    valor = models.IntegerField(null=True, blank=True)
    activo = models.BooleanField()
    descripcion = models.TextField(max_length=255, null=True, blank=True)
    pozo = models.ForeignKey(pozos, on_delete=models.CASCADE)

    #__Datos_Pozos_FIELDS__END

    class Meta:
        verbose_name        = _("Datos_Pozos")
        verbose_name_plural = _("Datos_Pozos")



#__MODELS__END
