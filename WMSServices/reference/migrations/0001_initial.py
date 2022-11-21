# Generated by Django 4.1.3 on 2022-11-18 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('name', models.CharField(max_length=255, verbose_name='Referencia')),
                ('model_size', models.CharField(max_length=100, verbose_name='Talla')),
                ('color', models.CharField(max_length=255, verbose_name='Color')),
            ],
        ),
    ]