# Generated by Django 4.1.7 on 2023-03-05 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=50, null=True)),
                ('Phone', models.DecimalField(decimal_places=0, max_digits=10)),
                ('Adress', models.CharField(blank=True, max_length=50, null=True)),
                ('Email', models.CharField(blank=True, max_length=50, null=True)),
                ('createdTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
