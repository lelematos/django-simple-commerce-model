# Generated by Django 3.0.8 on 2020-07-14 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_item_publicado'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='tamanhos',
            field=models.CharField(blank=True, choices=[('p', 'P'), ('m', 'M'), ('g', 'G')], max_length=1, null=True),
        ),
    ]
