# Generated by Django 5.0.6 on 2024-07-26 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyShopApp', '0010_remove_product_user_order_items_json'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_Update',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(default='')),
                ('update_desc', models.CharField(max_length=5000)),
                ('time_stamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
