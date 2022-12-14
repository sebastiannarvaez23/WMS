# Generated by Django 4.1.3 on 2022-11-20 06:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reference', '0003_alter_reference_options'),
        ('saleorder', '0002_alter_collection_options_alter_payterm_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='saleorderitem',
            name='sale_order',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='saleorder.saleorder', verbose_name='Orden de venta'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='saleorderitem',
            name='referece',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='reference.reference', verbose_name='Referencia'),
        ),
    ]
