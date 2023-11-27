# Generated by Django 4.2.7 on 2023-11-26 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('action', models.CharField(choices=[('NO_FILTER', 'No Filter'), ('COLORIZED', 'Colorized'), ('GRAYSCALE', 'Grayscale'), ('BLURRED', 'Blurred'), ('BINARY', 'Binary'), ('INVERTED', 'Inverted')], max_length=50)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]