from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Reads
from .serializer import ReadSerializer
from rest_framework import status
from rest_framework import generics

class CreateReadAPIView(APIView):
    def post(self, request):
        if request.method == "POST":
             serializer = ReadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
     if request.method == "GET":
           return Response({"error": "No data"}, status=200)
     
class ReadListAPIView(APIView):
    def get(self, request):
        if request.method == "GET":
            reads = Reads.objects.all()
            serializer = ReadSerializer(reads, many=True)
            return Response(serializer.data)

class DeleteAPIView(generics.DestroyAPIView):
    def delete(self,request,id):
        if request.method == "DELETE":
            reads = Reads.objects.get(id = id)
            if reads:
                reads.delete()
                return Response({"message":"successfully deleted"})
            else:
                return Response({"error":"Id does not exsist"})
           
       
        