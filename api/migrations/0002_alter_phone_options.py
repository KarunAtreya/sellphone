# Generated by Django 4.1 on 2022-09-16 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='phone',
            options={'ordering': ['id']},
        ),
    ]
