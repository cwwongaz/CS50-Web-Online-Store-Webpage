# Generated by Django 3.0.8 on 2020-09-06 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webstore', '0002_auto_20200905_0507'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='number_of_rating',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_brand',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_name',
            field=models.CharField(max_length=500),
        ),
    ]
