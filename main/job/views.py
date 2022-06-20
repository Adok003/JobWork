from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated


from .models import Employees
from .serializers import EmployeesSerializer


class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer
    permission_classes = (IsAuthenticated, )
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('manager_id', 'full_name', 'position', 'hire_date', 'salary')

