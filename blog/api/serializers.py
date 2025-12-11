from .models import StudentModels
from employeeApp.models import EmployeeModel
from rest_framework import serializers

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = StudentModels
        fields = '__all__'


class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeModel
        fields = '__all__'