# Generated by Django 5.1 on 2024-12-10 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_item_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://shorturl.at/XowF5', max_length=500),
        ),
    ]
