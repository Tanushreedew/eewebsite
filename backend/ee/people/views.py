from rest_framework.views import APIView
from .serializer import BTechSerializer, MTechSerializer, FacultySerializer, AlumniSerializer, PhdSerializer, StaffSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import BTech, Faculty, Staff, MTech, Alumni, Phd, MS
# from .manager import btech
# Create your views here.
import os
from .models import BTech, MTech, Faculty, Staff, Alumni, Phd
from PIL import Image

from django.core.files import File
from django.core.files.images import ImageFile


# def btech():
#     direct = os.listdir(r'D:\projects\ee-iiti\backend\ee\people\image')
#     print(direct)
#     df = pd.read_csv(r'D:\projects\ee-iiti\backend\ee\research\data.csv')
#     roll_list = df.roll_no.tolist()
#     for i in range(len(direct)):
#         image_path = f"D://projects//ee-iiti//backend//ee//people//image//{direct[i]}"
#         im = open(image_path, 'rb')
#         django_file = File(im)
#     #     # print(django_file)
#         django_image_file = ImageFile(im)
#         btech = BTech.objects.get(roll_no=roll_list[i])
#         print("sfkshdkjhskfhdkusahd")
#         btech.image.save(f'{roll_list[i]}.jpg', django_file, save=True)
#     #     # print(btech.image)
#         im.close()
#         # obj = serializer.save(created_by=self.request.user) aise karrrr haaa ruk naaa
#         btech.save(update_fields=['image'])


# class PeopleView(APIView):
#     def post(self, request):
#         if request.method == "POST":
#             serializer = PeopleSerializer(data=request.data)
#             if serializer.is_valid():
#                 data = serializer.create(request.data)
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         return Response({"message": "{} method is not allowed".format(request.method)})


class GetFacultyView(APIView):
    def get(self, request):
        if request.method == "GET":
            try:
                faculty = Faculty.objects.all()
            except Faculty.DoesNotExist:
                return Response({"error": "No faculty"}, status=404)
            faculty = FacultySerializer(faculty, many=True)
            return Response(faculty.data)
        return Response({"message": "{} method is not allowed".format(request.method)})


class GetStaffView(APIView):
    def get(self, request):
        if request.method == "GET":
            try:
                staff = Staff.objects.all()
            except Staff.DoesNotExist:
                return Response({"error": "No staff"}, status=404)
            staff = StaffSerializer(staff, many=True)
            return Response(staff.data)
        return Response({"message": "{} method is not allowed".format(request.method)})


class GetPhdByYear(APIView):
    def get(self, request, year):
        if request.method == "GET":
            try:
                phd = Phd.objects.filter(year=year).values()
            except Phd.DoesNotExist:
                return Response({"error": "No phd"}, status=404)
            return Response(phd)
        return Response({"message": "{} method is not allowed".format(request.method)})


class GetBtechByYear(APIView):
    def get(self, request, year):
        # faculty()
        if request.method == "GET":
            try:
                btech = BTech.objects.filter(year=year).values()
                print(btech)
            except BTech.DoesNotExist:
                return Response({"error": "No btech"}, status=404)
            return Response(btech)
        return Response({"message": "{} method is not allowed".format(request.method)})


class GetMtechByYear(APIView):
    def get(self, request, year):
        if request.method == "GET":
            try:
                mtech = MTech.objects.filter(year=year).values()
            except MTech.DoesNotExist:
                return Response({"error": "No mtech"}, status=404)
            return Response(mtech)
        return Response({"message": "{} method is not allowed".format(request.method)})


class GetAlumniByYear(APIView):
    def get(self, request, year):
        if request.method == "GET":
            try:
                alumni = Alumni.objects.filter(year=year).values()
            except Alumni.DoesNotExist:
                return Response({"error": "No alumni"}, status=404)
            return Response(alumni)
        return Response({"message": "{} method is not allowed".format(request.method)})


class GetMSByYear(APIView):
    def get(self, request, year):
        if request.method == "GET":
            try:
                ms = MS.objects.filter(year=year).values()
            except MS.DoesNotExist:
                return Response({"error": "No MS"}, status=404)
            return Response(ms)
        return Response({"message": "{} method is not allowed".format(request.method)})
