from rest_framework import serializers
from .models import Course, Elective, CourseNew

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
    
    def create(self,validated_data):
        course = Course.objects.create(program=validated_data.get('program'),
                                           semester=validated_data.get('semester'),
                                           credit=validated_data.get('credit'),
                                           ltp=validated_data('ltp'),
                                         name=validated_data.get('name'),
                                           code=validated_data.get('code'))
        return course


class CourseSerializerNew(serializers.ModelSerializer):
    class Meta:
        model = CourseNew
        fields = '__all__'
    
    def create(self,validated_data):
        course = CourseNew.objects.create(program=validated_data.get('program'),
                                           semester=validated_data.get('semester'),
                                         name=validated_data.get('name'),
                                           credit=validated_data.get('credit'),
                                           ltp=validated_data('ltp'),
                                         elective=validated_data.get('elective'),
                                           code=validated_data.get('code'))
        return course



class ElectiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elective
        fields = '__all__'

    def create(self, validated_data):
        elective = Elective.objects.create(program=validated_data.get('program'),
                                       name=validated_data.get('name'),
                                       code=validated_data.get('code'),
                                       credit=validated_data.get('credit'),
                                        ltp=validated_data('ltp'))
        return elective
