# Generated by Django 4.1.3 on 2022-11-20 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saleorder', '0003_saleorderitem_sale_order_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='saleorderitem',
            old_name='referece',
            new_name='reference',
        ),
    ]
