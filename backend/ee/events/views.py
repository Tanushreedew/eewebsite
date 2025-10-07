from rest_framework.views import APIView
from .serializer import EventsSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Events
# Create your views here.
class EventViews(APIView):
    def post(self,request):
        if request.method=='POST':
            serializer = EventsSerializer(data=request.data)
            if serializer.is_valid():
                data = serializer.create(request.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "{} method is not allowed".format(request.method)})
    

class GetEventView(APIView):
    def get(self, request):
        if request.method == "GET":
            try:
                event = Events.objects.all()
            except event.DoesNotExist:
                return Response({"error": "No announcements"}, status=404)
            event = EventsSerializer(event, many=True)
            return Response(event.data)
        return Response({"message": "{} method is not allowed".format(request.method)})
