# Generated by Django 3.2.9 on 2021-11-20 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usertype',
            name='uername',
        ),
    ]