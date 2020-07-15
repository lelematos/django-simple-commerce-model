# Generated by Django 3.0.8 on 2020-07-13 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descricao', models.CharField(max_length=2000)),
                ('data de publicação', models.DateTimeField(auto_now=True)),
                ('preco', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('preco_com_desconto', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('img1', models.ImageField(blank=True, null=True, upload_to='uploaded_images')),
            ],
        ),
    ]
