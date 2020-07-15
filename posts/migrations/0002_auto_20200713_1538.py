# Generated by Django 3.0.8 on 2020-07-13 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='data de publicação',
        ),
        migrations.AddField(
            model_name='item',
            name='data_publicacao',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='img1',
            field=models.ImageField(blank=True, null=True, upload_to='static/uploaded_images'),
        ),
    ]