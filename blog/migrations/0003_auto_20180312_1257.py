# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-03-12 03:57
from __future__ import unicode_literals

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180312_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default='anonymous', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='lnglat',
            field=models.CharField(blank=True, help_text='위도/경도 포맷으로 입력', max_length=50, validators=[blog.models.lnglat_validator]),
        ),
    ]
