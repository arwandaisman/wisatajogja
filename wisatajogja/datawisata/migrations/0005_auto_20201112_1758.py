# Generated by Django 2.2.17 on 2020-11-12 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datawisata', '0004_datawisata_lokasi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datawisata',
            name='nama_wisata',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
