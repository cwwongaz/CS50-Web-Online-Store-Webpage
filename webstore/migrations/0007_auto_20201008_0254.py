# Generated by Django 3.0.8 on 2020-10-08 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webstore', '0006_auto_20201006_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='picture',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
