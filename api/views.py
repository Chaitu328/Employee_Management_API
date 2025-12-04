from django.shortcuts import render
from rest_framework.views import APIView
from employees.models import Employee
from .serializer import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework import mixins,generics,viewsets
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from employees.filters import EmployeeFilter
from rest_framework import filters
# Create your views here.
# class Employees(APIView):
#     def get(self,request):
#         employees = Employee.objects.all()
#         serializer = EmployeeSerializer(employees,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     def post(self,request):
#         serializer = EmployeeSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# class EmployeeDetail(APIView):
#     def get_object(self,pk):
#         return get_object_or_404(Employee,pk=pk)
    
#     def get(self,request,pk):
#         employees = self.get_object(pk)
#         serializer = EmployeeSerializer(employees)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def put(self,request,pk):
#         employees = self.get_object(pk)
#         serializer = EmployeeSerializer(employees,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#     def delete(self,request,pk):
#         employees = self.get_object(pk)
#         employees.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
# Mixins
# class Employees(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

#     def get(self, request):
#         return self.list(request)
    
#     def post(self,request):
#         return self.create(request)

# class EmployeeDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

#     def get(self,request,pk):
#         return self.retrieve(request,pk)
    
#     def put(self,request,pk):
#         return self.update(request,pk)
    
#     def delete(self,request,pk):
#         return self.destroy(request,pk)
    

# Generics
# class Employees(generics.ListCreateAPIView):
#     queryset =Employee.objects.all()
#     serializer_class = EmployeeSerializer

#     def create(self,request,*args,**kwargs):
#         data =request.data

#         if isinstance(data,list):
#             serializer = self.get_serializer(data=data,many=True)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data,status=status.HTTP_201_CREATED)
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#         return super().create(request,*args,**kwargs)


# class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer


# viewset
class EmployeeViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [SearchFilter,filters.OrderingFilter,DjangoFilterBackend]
    search_fields = ['name']
    filterset_class = EmployeeFilter
    ordering_fields = ['name','salary','date_joined']