# Generated by Django 3.0.8 on 2020-07-14 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_item_variações'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='variações',
            new_name='variacoes',
        ),
    ]