from rest_framework import serializers
from .models import Reads

class ReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reads
        fields ='__all__'

    def create(self,validated_data):
        read = Reads.objects.create(
            title = validated_data.get('title'),
            content = validated_data.get('content'),
            author = validated_data.get('author')
        )
        return read
        