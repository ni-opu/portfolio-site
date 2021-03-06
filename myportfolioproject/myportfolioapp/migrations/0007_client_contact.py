# Generated by Django 3.2 on 2021-05-12 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolioapp', '0006_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('client_logo', models.ImageField(upload_to='img/logo/')),
                ('client_link', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('messages', models.TextField()),
            ],
        ),
    ]
