from django.contrib import admin
from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    model = Employee
    fields = ('employee_identification', 'employee_name','active',)
    list_display = ['employee_identification','employee_name','active',]
    actions = ['status']
    readonly_fields = []

    #for i in Employee.objects.values_list('pk')):

    for i in Employee.objects.all():
        if i.active:
            readonly_fields.append('employee_identification')
        else:
            print('there is nothing here')


admin.site.register(Employee, EmployeeAdmin)
