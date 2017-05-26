# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-26 16:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='ToolType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tool_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='tool',
            name='tool_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tools.ToolType'),
        ),
    ]
