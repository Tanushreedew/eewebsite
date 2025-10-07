from rest_framework.views import APIView
from .serializer import NewsSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import News
# Create your views here.


class NewsView(APIView):
    def post(self, request):
        if request.method == "POST":
            serializer = NewsSerializer(data=request.data)
            if serializer.is_valid():
                data = serializer.create(request.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "{} method is not allowed".format(request.method)})


class GetNewsView(APIView):
    def get(self, request):
        if request.method == "GET":
            try:
                news = News.objects.all()
            except news.DoesNotExist:
                return Response({"error": "No News"}, status=404)
            news = NewsSerializer(news, many=True)
            return Response(news.data)
        return Response({"message": "{} method is not allowed".format(request.method)})
