# Generated by Django 3.2.11 on 2022-02-18 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salaryslip', '0005_alter_employee_employee_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='salary_breakup',
            field=models.JSONField(max_length=2000),
        ),
    ]
