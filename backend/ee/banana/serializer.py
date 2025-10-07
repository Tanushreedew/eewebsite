from rest_framework import serializers
from .models import Banana

class BananaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banana
        fields = '__all__'
    
    def create(self,validated_data):
        course = Banana.objects.create(name=validated_data.get('name'),
                                           price=validated_data.get('price'))
        return course

