# Generated by Django 4.1.7 on 2023-03-05 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_alter_customers_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='Phone',
            field=models.BigIntegerField(null=True),
        ),
    ]
