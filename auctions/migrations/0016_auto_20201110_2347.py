# Generated by Django 3.1.2 on 2020-11-10 23:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0015_auto_20201110_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorya',
            name='listing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='is_cata', to='auctions.listing'),
        ),
        migrations.AlterField(
            model_name='categoryb',
            name='listing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='is_catb', to='auctions.listing'),
        ),
        migrations.AlterField(
            model_name='categoryc',
            name='listing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='is_catc', to='auctions.listing'),
        ),
    ]