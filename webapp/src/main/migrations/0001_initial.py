# Generated by Django 4.1.1 on 2022-09-14 01:46

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
                ('name', models.CharField(max_length=250, verbose_name='Name')),
                ('description', models.CharField(max_length=500, verbose_name='Description')),
                ('price', models.IntegerField(verbose_name='Price')),
            ],
        ),
    ]
