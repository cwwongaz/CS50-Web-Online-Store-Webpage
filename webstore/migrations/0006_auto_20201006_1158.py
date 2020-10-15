# Generated by Django 3.0.8 on 2020-10-06 11:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webstore', '0005_auto_20200923_0212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='rater',
        ),
        migrations.AddField(
            model_name='rating',
            name='rater',
            field=models.ForeignKey(default=123, on_delete=django.db.models.deletion.CASCADE, related_name='user_rating', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]