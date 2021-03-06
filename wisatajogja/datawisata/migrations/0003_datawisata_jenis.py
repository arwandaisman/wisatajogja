# Generated by Django 2.2.17 on 2020-11-12 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('datawisata', '0002_delete_datawisata'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jenis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jenis', models.CharField(max_length=9)),
                ('keterangan', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Datawisata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_wisata', models.CharField(max_length=20, null=True)),
                ('kabupaten', models.CharField(max_length=20, null=True)),
                ('jml_pengunjung', models.IntegerField(null=True)),
                ('jenis_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datawisata.Jenis')),
            ],
        ),
    ]
