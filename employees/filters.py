import django_filters
from .models import Employee

class EmployeeFilter(django_filters.FilterSet):
    designation = django_filters.CharFilter(field_name='designation')
    id = django_filters.RangeFilter(field_name='id')
    salary = django_filters.RangeFilter(field_name='salary')
    class Meta:
        model = Employee
        fields = ['designation','id','salary']
