# Generated by Django 3.2 on 2021-05-12 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fa_icon_calss', models.CharField(max_length=200)),
                ('service_name', models.CharField(max_length=100)),
                ('service_details', models.TextField()),
            ],
        ),
    ]
