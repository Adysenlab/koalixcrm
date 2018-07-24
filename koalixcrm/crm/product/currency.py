# -*- coding: utf-8 -*-

from django.db import models
from django.contrib import admin
from django.utils.translation import ugettext as _
from rest_framework import serializers


class Currency(models.Model):
    description = models.CharField(verbose_name=_("Description"), max_length=100)
    short_name = models.CharField(verbose_name=_("Displayed Name After Price In The Position"), max_length=3)
    rounding = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_("Rounding"), blank=True, null=True)

    def __str__(self):
        return self.short_name

    class Meta:
        app_label = "crm"
        verbose_name = _('Currency')
        verbose_name_plural = _('Currency')


class OptionCurrency(admin.ModelAdmin):
    list_display = ('id', 'description', 'short_name', 'rounding')
    fieldsets = (('', {'fields': ('description', 'short_name', 'rounding')}),)
    allow_add = True


class CurrencyJSONSerializer(serializers.HyperlinkedModelSerializer):
    shortName = serializers.CharField(source='short_name')

    class Meta:
        model = Currency
        fields = ('id',
                  'description',
                  'shortName',
                  'rounding')
