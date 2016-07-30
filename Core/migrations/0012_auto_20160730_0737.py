# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-30 07:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0011_auto_20160729_2123'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ContactForm',
        ),
        migrations.AlterModelOptions(
            name='contactus',
            options={'verbose_name_plural': 'contact us'},
        ),
        migrations.RenameField(
            model_name='contactus',
            old_name='phone',
            new_name='contact',
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='file',
        ),
        migrations.AlterField(
            model_name='contactus',
            name='email',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='message',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='subject',
            field=models.CharField(max_length=255),
        ),
    ]