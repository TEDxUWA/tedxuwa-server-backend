# Generated by Django 2.0.4 on 2018-05-05 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_auto_20180503_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]