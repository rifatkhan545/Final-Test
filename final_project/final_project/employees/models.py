from django.db import models


class Employee(models.Model):
    employee_identification = models.CharField(max_length= 40,  unique=True, null=True, blank= True, verbose_name= 'employee_identification')
    employee_name = models.CharField(max_length=40, blank= True, )
    active = models.BooleanField(default= False)




    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def __str__(self):
        return self.employee_name
