# Generated by Django 4.1.7 on 2023-03-13 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_customers_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='image',
            field=models.ImageField(default='/placeholder.png', upload_to=''),
        ),
    ]
