# Generated by Django 3.1.1 on 2020-09-19 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mystore', '0006_auto_20200919_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(),
        ),
    ]
