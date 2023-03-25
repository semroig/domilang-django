from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer, StudentSerializer, TeacherSerializer, ClaseSerializer, DisponibleSerializer, PaymentSerializer
from ..models import User, Student, Teacher, Clase, Disponible, Payment


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = UserSerializer

class StudentViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class ClaseViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Clase.objects.all()
    serializer_class = ClaseSerializer

    def get_queryset(self):
        queryset = Clase.objects.all()
        
        # Filtro por dia
        day = self.request.query_params.get('day')
        if day is not None:
            queryset = queryset.filter(dia=day)
        
        # Filtro por teacher
        teacher = self.request.query_params.get('teacher')
        if teacher is not None:
            queryset = queryset.filter(teacher=teacher)

        return queryset

class DisponibleViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Disponible.objects.all()
    serializer_class = DisponibleSerializer

    def get_queryset(self):
        queryset = Disponible.objects.all()
        
        # Filtro por dia
        day = self.request.query_params.get('day')
        if day is not None:
            queryset = queryset.filter(dia=day)
        
        # Filtro por teacher
        teacher = self.request.query_params.get('teacher')
        if teacher is not None:
            queryset = queryset.filter(teacher=teacher)

        return queryset

class PaymentViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer