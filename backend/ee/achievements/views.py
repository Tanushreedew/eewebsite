from rest_framework.views import APIView
from .serializer import BooksSerializer, StudentAwardsSerializer, FacultyAwardsSerializer, PatentSerializer
from rest_framework.response import Response
from .models import Books,StudentAwards,FacultyAwards, Patent

class GetBooksAPI(APIView):
    def get(self, request):
        if request.method == "GET":
            try:
                books = Books.objects.all()
            except books.DoesNotExist:
                return Response({"error": "No   books"}, status=404)
            books = BooksSerializer(books, many=True)
            return Response(books.data)
        return Response({"message": "{} method is not allowed".format(request.method)})


class GetStudentAwardsAPI(APIView):
    def get(self, request):
        if request.method == "GET":
            try:
                student = StudentAwards.objects.all()
            except student.DoesNotExist:
                return Response({"error": "No   student"}, status=404)
            student = StudentAwardsSerializer(student, many=True)
            return Response(student.data)
        return Response({"message": "{} method is not allowed".format(request.method)})


class GetFacultyAwardsAPI(APIView):
    def get(self, request):
        if request.method == "GET":
            try:
                faculty = FacultyAwards.objects.all()
            except faculty.DoesNotExist:
                return Response({"error": "No   faculty"}, status=404)
            faculty = FacultyAwardsSerializer(faculty, many=True)
            return Response(faculty.data)
        return Response({"message": "{} method is not allowed".format(request.method)})

class GetPatentAPI(APIView):
    def get(self, request):
        if request.method == "GET":
            try:
                patent = Patent.objects.all()
            except patent.DoesNotExist:
                return Response({"error": "No   patent"}, status=404)
            patent = PatentSerializer(patent, many=True)
            return Response(patent.data)
        return Response({"message": "{} method is not allowed".format(request.method)})
