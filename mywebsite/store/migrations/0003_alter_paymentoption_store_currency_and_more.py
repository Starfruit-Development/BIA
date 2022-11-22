# Generated by Django 4.1.2 on 2022-11-21 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_paymentoption_store_currency_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentoption',
            name='store_currency',
            field=models.CharField(choices=[('eur', 'Eur'), ('dollars', 'Dollars')], default='eur', max_length=10),
        ),
        migrations.AlterField(
            model_name='store',
            name='store_industry',
            field=models.CharField(choices=[('Fashion', 'Fashion'), ('clothing', 'Clothing'), ('jewelry', 'Jewelry')], default='Fashion', max_length=50),
        ),
    ]
