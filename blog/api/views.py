from django.shortcuts import render
from django.http import JsonResponse, Http404
from rest_framework.response import Response

from .models import StudentModels
from .serializers import StudentSerializers
from rest_framework.decorators import api_view
from rest_framework import status
from employeeApp.models import EmployeeModel
from .serializers import employeeSerializer
from rest_framework.views import APIView
from rest_framework import mixins,generics,viewsets
from QuoteApp.serializers import authorSerializer,quoteSerializer
from QuoteApp.models import AuthorModel,QuoteModel
from .pagination import MyCustomPageNumberPagination
from .filters import EmployeeFilter
# from rest_framework.generics import *
from rest_framework.filters import SearchFilter,OrderingFilter
# Create your views here.


@api_view(["GET","POST"])
def studentView(request):
    if request.method == "GET":
       student = StudentModels.objects.all()
       serializer = StudentSerializers(student,many=True)
       return Response(serializer.data, status = status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = StudentSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET","PUT","DELETE"])
def studentMoreInfo(request,pk):
    try:
        student = StudentModels.objects.get(pk=pk)
    except:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = StudentSerializers(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = StudentSerializers(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



#
# class EmployeeViewData(APIView):
#     def get(self,request):
#         model = EmployeeModel.objects.all()
#         serializer = employeeSerializer(model, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self,request):
#         serializer = employeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class EmployeeObjectView(APIView):
#     def get_object(self,pk):
#         try:
#             return  EmployeeModel.objects.get(pk=pk)
#
#         except EmployeeModel.DoesNotExist:
#             raise Http404
#
#
#     def get(self,request,pk):
#         employee = self.get_object(pk)
#         serializer = employeeSerializer(employee)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#
#     def put(self,request,pk):
#         employee = self.get_object(pk)
#         serializer= employeeSerializer(employee,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self,request,pk):
#         employee = self.get_object(pk)
#         employee.delete()
#         return Response(status=status.HTTP_410_GONE)
#
# class EmployeeViewData(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = EmployeeModel.objects.all()
#     serializer_class = employeeSerializer
#
#     def get(self,request):
#         return self.list(request)
#
#
#     def post(self,request):
#         return self.create(request)
#
# class EmployeeObjectView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = EmployeeModel.objects.all()
#     serializer_class = employeeSerializer
#
#     def get(self,request,pk):
#         return self.retrieve(request,pk)
#
#     def put(self,request,pk):
#         return self.update(request,pk)
#
#     def delete(self,request,pk):
#         return self.destroy(request,pk)



# class EmployeeViewData(generics.ListAPIView,generics.CreateAPIView):
#       queryset = EmployeeModel.objects.all()
#       serializer_class = employeeSerializer
#


class EmployeeViewData(generics.ListCreateAPIView):
    queryset = EmployeeModel.objects.all()
    serializer_class = employeeSerializer


class EmployeeObjectView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployeeModel.objects.all()
    serializer_class = employeeSerializer
    lookup_field = "pk"




# class EmployeeInfoView(viewsets.ViewSet):
#     def list(self,request):
#         queryset = EmployeeModel.objects.all()
#         serializer = employeeSerializer(queryset,many=True)
#         return Response(serializer.data)
#
#
#     def create(self,request):
#         serializer = employeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
#
#     def retrieve(self,request,pk=None):
#         queryset = EmployeeModel.objects.get(pk=pk)
#         serializer = employeeSerializer(queryset)
#         return Response(serializer.data,status=status.HTTP_200_OK)
#
#


class EmployeeInfoView(viewsets.ModelViewSet):
    queryset = EmployeeModel.objects.all()
    serializer_class = employeeSerializer
    pagination_class = MyCustomPageNumberPagination
    # filterset_fields = ["designation"]
    filterset_class = EmployeeFilter


#
#
#


class AuthorView(generics.ListCreateAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = authorSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['authorDescription','authorName']
    ordering_fileds = ['id']

class QuoteView(generics.ListCreateAPIView):
    queryset = QuoteModel.objects.all()
    serializer_class = quoteSerializer






