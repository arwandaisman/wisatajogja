# Generated by Django 2.2.17 on 2020-11-12 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_datawisata_id_wisata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datawisata',
            name='detail',
        ),
        migrations.RemoveField(
            model_name='datawisata',
            name='jenis',
        ),
        migrations.AddField(
            model_name='datawisata',
            name='lokasi',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
