# Generated by Django 3.0.8 on 2020-09-23 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webstore', '0004_auto_20200913_0711'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_footnote',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_Description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_name',
            field=models.CharField(max_length=100),
        ),
    ]
