import django_filters
from employeeApp.models import EmployeeModel

class EmployeeFilter(django_filters.FilterSet):
    designation = django_filters.CharFilter(field_name="designation",lookup_expr='iexact')
    empName = django_filters.CharFilter(field_name="empName", lookup_expr="icontains")
    class Meta:
        model = EmployeeModel
        fields = ["designation","empName"]

