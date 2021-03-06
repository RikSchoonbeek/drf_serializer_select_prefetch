# Generated by Django 4.0 on 2022-02-20 20:20

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organization', '0001_create_organization_unit_employee_models'),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.SmallIntegerField(blank=True, unique=True)),
                ('start_date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='case.case')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.employee')),
            ],
        ),
    ]
