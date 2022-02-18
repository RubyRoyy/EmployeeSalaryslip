import json
from django.forms import model_to_dict
from django.http import JsonResponse
from .models import Employee, Department, Designation


def create_employee(request):
    body = json.loads(request.body.decode("utf-8"))
    department = Department.objects.get(id=body["department"].get("id"))
    designation = Designation.objects.get(id=body["designation"]["id"])
    body["department"] = department
    body["designation"] = designation
    body["salary_breakup"] = get_employee_salary_breakup(body["fixed_anual_ctc"])
    employee, created = Employee.objects.get_or_create(**body)
    return JsonResponse(model_to_dict(employee))


def get_employees(request):
    employees = Employee.objects.all()
    return JsonResponse(list(employees.values()), safe=False)


def get_employee_salary_breakup(ctc):
    data = {}
    if not ctc:
        return data

    basic = 0.25 * ctc
    hra = 0.25 * basic
    lta = 1000  # asume 1000
    other_allownaces = 4500
    data["earnings"] = {
        "basic": basic,
        'hra': hra,
        "lta": lta,
        "other_allowances": other_allownaces,
        "gross_earnings": ctc,
    }
    food_deduction = 2000
    tds = 0.10 * ctc
    gross_deduction = 0.10 * ctc + food_deduction
    data["deductions"] = {
        "TDS": tds,
        "food": food_deduction,
        "gross_deduction": gross_deduction
    }
    data["net_pay"] = ctc - gross_deduction
    return data
