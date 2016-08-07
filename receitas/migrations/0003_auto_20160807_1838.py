# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-07 18:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0002_auto_20160807_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='ingrediente',
            field=models.ManyToManyField(blank=True, to='receitas.Ingrediente'),
        ),
        migrations.AlterField(
            model_name='receita',
            name='modo_preparo',
            field=models.ManyToManyField(blank=True, to='receitas.Preparo'),
        ),
    ]