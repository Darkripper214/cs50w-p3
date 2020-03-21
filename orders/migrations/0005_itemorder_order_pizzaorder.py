# Generated by Django 3.0.4 on 2020-03-20 10:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0004_pizza_max_topping'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Processing', 'Processing'), ('Completed', 'Completed')], max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PizzaOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topping', models.IntegerField(default=0)),
                ('order_price', models.DecimalField(decimal_places=2, help_text='Price in USD', max_digits=5)),
                ('order_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Order')),
                ('pizza_ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Pizza')),
            ],
        ),
        migrations.CreateModel(
            name='ItemOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_price', models.DecimalField(decimal_places=2, help_text='Price in USD', max_digits=5)),
                ('item_ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Item')),
                ('order_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Order')),
            ],
        ),
    ]
