# Generated by Django 2.2.17 on 2020-11-12 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datawisata', '0003_datawisata_jenis'),
    ]

    operations = [
        migrations.AddField(
            model_name='datawisata',
            name='lokasi',
            field=models.CharField(max_length=50, null=True),
        ),
    ]