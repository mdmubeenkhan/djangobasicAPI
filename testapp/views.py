from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from io import BytesIO
from rest_framework.parsers import JSONParser

# Create your views here.
class EmployeeView(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeAPIView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Employee.objects.all()
        serializer = EmployeeSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        emp_serializer = EmployeeSerializer(data=python_data)
        if emp_serializer.is_valid():
            emp_serializer.save()
            return Response('Employee record inserted.')        
        return Response(emp_serializer.errors)

    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = BytesIO(json_data)
        python_data = JSONParser().parse(stream=stream)
        emp_no = python_data.get('eno')
        emp_obj = Employee.objects.get(eno=emp_no)
        emp_serializer = EmployeeSerializer(emp_obj, data=python_data, partial=True)
        if emp_serializer.is_valid():
            emp_serializer.save()
            return Response('Employee record updated.')        
        return Response(emp_serializer.errors)

    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = BytesIO(json_data)
        python_data = JSONParser().parse(stream=stream)
        emp_no = python_data.get('eno')
        emp_obj = Employee.objects.get(eno=emp_no)
        emp_obj.delete()
        return Response('Employee record deleted.')  
