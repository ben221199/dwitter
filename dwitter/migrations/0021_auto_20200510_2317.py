# Generated by Django 2.2.8 on 2020-05-10 23:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dwitter', '0020_auto_20191204_0418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dweet',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked', to=settings.AUTH_USER_MODEL),
        ),
    ]
