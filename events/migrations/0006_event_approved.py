# Generated by Django 3.1.5 on 2022-01-11 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_venue_venue_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='approved',
            field=models.BooleanField(default=False, verbose_name='Aprroved'),
        ),
    ]
