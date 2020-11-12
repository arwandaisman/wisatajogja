# Generated by Django 2.2.17 on 2020-11-12 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Datawisata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_wisata', models.CharField(max_length=20, null=True)),
                ('nama_wisata', models.CharField(max_length=20, null=True)),
                ('kabupaten', models.CharField(max_length=20, null=True)),
                ('jenis', models.CharField(max_length=15, null=True)),
                ('detail', models.TextField(null=True)),
            ],
        ),
    ]