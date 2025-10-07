from rest_framework import serializers
from .models import Books, StudentAwards, FacultyAwards, Patent

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'

    def create(self,validated_data):
        Book = Books.objects.create(name=validated_data.get('name'),
                                           year=validated_data.get('year'),
                                           author=validated_data.get('author'),
                                    publication=validated_data.get('publication'),
                                    image=validated_data.get('image'))
        return Book


class StudentAwardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAwards
        fields = '__all__'

    def create(self, validated_data):
        student = StudentAwards.objects.create(name=validated_data.get('name'),
                                    year=validated_data.get('year'),
                                    award=validated_data.get('award'),
                                    roll_no=validated_data.get(
                                        'roll_no'),
                                    image=validated_data.get('image'))
        return student


class FacultyAwardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacultyAwards
        fields = '__all__'

    def create(self, validated_data):
        faculty = FacultyAwards.objects.create(name=validated_data.get('name'),
                                    year=validated_data.get('year'),
                                    award=validated_data.get('award'),
                                    roll_no=validated_data.get('roll_no'),
                                    image=validated_data.get('image'))
        return faculty



class PatentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patent
        fields = '__all__'

    def create(self, validated_data):
        patent = Patent.objects.create(name=validated_data.get('name'),
                                    year=validated_data.get('year'),
                                    pi=validated_data.get('pi'),
                                    uuid=validated_data.get('uuid'),
                                    status=validated_data.get('status'))                                                                                                                                                                                           
        return patent