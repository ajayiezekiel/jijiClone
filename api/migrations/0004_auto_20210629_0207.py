# Generated by Django 3.2.4 on 2021-06-29 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('vehicles', 'VEHICLES'), ('phones', 'PHONES'), ('property', 'PROPERTY'), ('electronics', 'ELECTRONICS'), ('fashion', 'FASHION')], default='phones', max_length=100),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
