# Generated by Django 3.1.1 on 2020-09-19 03:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20200916_2043'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('created',)},
        ),
    ]
