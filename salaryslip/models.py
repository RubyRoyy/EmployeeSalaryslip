from django.db import models


class Designation(models.Model):
    designation = models.CharField(max_length=100, null=False)


class Department(models.Model):
    name = models.CharField(max_length=100, null=False)


class Employee(models.Model):
    employee_name = models.CharField(max_length=64)
    employee_code = models.IntegerField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    designation = models.ForeignKey(Designation, on_delete=models.DO_NOTHING)
    joining_date = models.DateTimeField(null=True, blank=True)
    birth_date = models.DateTimeField(null=True, blank=True)
    bank_account_number = models.CharField(max_length=16, blank=True)
    no_of_leaves = models.IntegerField(default=21)
    pf_number = models.CharField(max_length=100, blank=True)
    fixed_anual_ctc = models.FloatField(blank=True, null=True)
    balance_leaves = models.IntegerField(blank=True, null=True)
    monthly_ctc = models.FloatField(blank=True, null=True)
    salary_breakup = models.JSONField(max_length=2000)

    def __str__(self):
        return " name-" + self.employee_name
