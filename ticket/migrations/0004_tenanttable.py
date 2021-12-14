# Generated by Django 3.2.9 on 2021-12-11 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0003_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='TenantTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenant_id', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mobile_number', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('start_day', models.DateField()),
                ('end_day', models.DateField()),
                ('status', models.CharField(max_length=100)),
                ('count_timer', models.IntegerField()),
            ],
        ),
    ]
