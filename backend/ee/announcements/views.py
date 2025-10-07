from rest_framework.views import APIView
from .serializer import AnnouncementSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Announcements
# Create your views here.
class AnnouncementViews(APIView):
    def post(self,request):
        if request.method=="POST":
            serializer = AnnouncementSerializer(data=request.data)
            if serializer.is_valid():
                data = serializer.create(request.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "{} method is not allowed".format(request.method)})


class GetAnnouncementsView(APIView):
    def get(self,request):
        if request.method=="GET":
            try:
                announcement = Announcements.objects.all()
            except announcement.DoesNotExist:
                return Response({"error":"No announcements"},status=404)
            announce = AnnouncementSerializer(announcement, many=True)
            return Response(announce.data)
        return Response({"message": "{} method is not allowed".format(request.method)})