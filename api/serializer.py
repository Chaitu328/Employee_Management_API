from employees.models import Employee
from rest_framework import serializers

class EmployeeSerializer(serializers.ModelSerializer):

    def validate_email(self, value):
        if not value.endswith('@company.com'):
            raise serializers.ValidationError('Email must be from company name')
        return value
    
    def validate_salary(self, value):
        if value <= 0:
            raise serializers.ValidationError('Salary must be Positive')
        return value
    
    def validate_emp_id(self, value):
        if not value.startswith('EMP'):
            raise serializers.ValidationError('emp_id starts with "EMP"')
        number = value[:3]
        if not number.isdigit  or len(number) == 0:
            raise serializers.ValidationError('emp_id must follow the format "EMP" followed by numbers')
        
        return value

    class Meta:
        model = Employee
        fields = '__all__'

