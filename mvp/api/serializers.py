from rest_framework import serializers

from ..models import User, Student, Teacher, Clase, Disponible, Payment


# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['url', 'country']

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['url', 'age']

class ClaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clase
        fields = '__all__'

class DisponibleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disponible
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'