# Generated by Django 5.1 on 2024-11-29 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=200)),
                ('item_desc', models.CharField(max_length=200)),
                ('item_price', models.IntegerField()),
            ],
        ),
    ]
