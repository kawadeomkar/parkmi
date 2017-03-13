# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-13 11:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parkingspot',
            name='zip',
        ),
        migrations.AddField(
            model_name='parkingspot',
            name='description',
            field=models.TextField(blank=True, default=b'', max_length=1000),
        ),
        migrations.AddField(
            model_name='parkingspot',
            name='picture',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='parkingspot',
            name='title',
            field=models.CharField(default=b'', max_length=25),
        ),
        migrations.AddField(
            model_name='parkingspot',
            name='zipcode',
            field=models.CharField(default=b'', max_length=5),
        ),
        migrations.AlterField(
            model_name='parkingspot',
            name='city',
            field=models.CharField(default=b'', max_length=15),
        ),
        migrations.AlterField(
            model_name='parkingspot',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='parkingspot',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='parkingspot',
            name='state',
            field=models.CharField(default=b'', max_length=2),
        ),
        migrations.AlterField(
            model_name='parkingspot',
            name='street',
            field=models.CharField(default=b'', max_length=50),
        ),
    ]