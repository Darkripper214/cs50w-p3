# Generated by Django 3.0.4 on 2020-03-20 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20200320_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='max_topping',
            field=models.IntegerField(default=0),
        ),
    ]
