# Generated by Django 3.0.8 on 2020-07-14 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_item_tamanhos'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='variações',
            field=models.BooleanField(default=False),
        ),
    ]
