# Generated by Django 3.1.2 on 2020-11-09 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_user_watchlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='watchlist',
            field=models.JSONField(default={}),
        ),
    ]
