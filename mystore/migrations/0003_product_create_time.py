# Generated by Django 3.1.1 on 2020-09-15 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mystore', '0002_product_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='create_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
