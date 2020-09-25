# Generated by Django 3.1.1 on 2020-09-22 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salinity', models.DecimalField(decimal_places=3, max_digits=8)),
                ('conductivity', models.DecimalField(decimal_places=3, max_digits=8)),
                ('temperature', models.DecimalField(decimal_places=3, max_digits=8)),
                ('depth', models.DecimalField(decimal_places=3, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Freq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frequency', models.DecimalField(decimal_places=3, max_digits=8)),
                ('attenuation', models.DecimalField(decimal_places=5, max_digits=8)),
                ('tech', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasman.technology')),
            ],
        ),
    ]
