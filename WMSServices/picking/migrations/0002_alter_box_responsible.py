# Generated by Django 4.1.3 on 2022-11-18 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='box',
            name='responsible',
            field=models.CharField(max_length=255, verbose_name='Responsable'),
        ),
    ]
