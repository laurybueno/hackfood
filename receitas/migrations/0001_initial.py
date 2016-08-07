# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-07 17:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Preparo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.TextField()),
                ('ingrediente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='receitas.Ingrediente')),
                ('modo_preparo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='receitas.Preparo')),
            ],
        ),
    ]