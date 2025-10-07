from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from news.models import News

# Create your views here.

class GetBananaView(APIView):
    def get(self, request):
        if request.method == "GET":
            try:
                course = News.objects.all().values()
                print(course)
            except News.DoesNotExist:
                return Response({"message": "Course of the required program and semester not found"}, status=status.HTTP_404_NOT_FOUND)
            return Response(course)
        return Response({"message": "{} method is not allowed".format(request.method)})
    