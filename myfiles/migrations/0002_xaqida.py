# Generated by Django 4.1.2 on 2023-01-13 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Xaqida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xonalar', models.CharField(max_length=10)),
                ('oshxona', models.CharField(max_length=10)),
                ('sport', models.CharField(max_length=10)),
                ('malumot', models.CharField(max_length=100)),
            ],
        ),
    ]