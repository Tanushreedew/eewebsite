from rest_framework import serializers
from .models import Staff, Faculty, MTech, BTech, Alumni, Phd, MS
from people.manager import im_to_base64


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'

    def create(self, validated_data):
        staff = Staff.objects.create(name=validated_data.get('name'),
                                     title=validated_data.get('title'),
                                     email=validated_data.get('email'),
                                     phone=validated_data.get('phone'),
                                     image=im_to_base64(validated_data.get('image')))
        return staff


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'

    def create(self, validated_data):
        faculty = Faculty.objects.create(name=validated_data.get('name'),
                                         place=validated_data.get('place'),
                                         title=validated_data.get('title'),
                                         subtitle=validated_data.get(
                                             'subtitle'),
                                         email=validated_data.get('email'),
                                         image=im_to_base64(
                                             validated_data.get('image')),
                                         details=validated_data.get('details'),
                                         address=validated_data.get('address'),
                                         link=validated_data.get('link'))
        return faculty


class MTechSerializer(serializers.ModelSerializer):
    class Meta:
        model = MTech
        fields = '__all__'

    def create(self, validated_data):
        mtech = MTech.objects.create(name=validated_data.get('name'),
                                     roll_no=validated_data.get('roll_no'),
                                     year=validated_data.get('year'),
                                     image=im_to_base64(validated_data.get('image')))
        return mtech


class BTechSerializer(serializers.ModelSerializer):
    class Meta:
        model = BTech
        fields = '__all__'

    def create(self, validated_data):
        btech = BTech.objects.create(name=validated_data.get('name'),
                                     roll_no=validated_data.get('roll_no'),
                                     year=validated_data.get('year'),
                                     image=validated_data.get('image'))
        return btech

    def update(self, validated_data, roll_no):
        try:
            btech = BTech.objects.get(
                roll_no=roll_no)
        except btech.DoesNotExist:
            raise ValueError("Event doesn't exist with given id")
        if validated_data.get('image'):
            event.title = validated_data.get('title')
        if validated_data.get('description'):
            event.description = validated_data.get('description')
        if validated_data.get('date'):
            event.date = validated_data.get('date')
        if validated_data.get('month'):
            event.month = validated_data.get('month')
        if validated_data.get('day'):
            event.day = validated_data.get('day')
        if validated_data.get('time'):
            event.time = validated_data.get('time')
        event.save(update_fields=[
                   'title', 'description', 'date', 'month', 'day', 'time'])
        return event


class PhdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phd
        fields = '__all__'

    def create(self, validated_data):
        phd = Phd.objects.create(name=validated_data.get('name'),
                                 details=validated_data.get('details'),
                                 roll_no=validated_data.get('roll_no'),
                                 year=validated_data.get('year'),
                                 image=im_to_base64(validated_data.get('image')))
        return phd


class AlumniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumni
        fields = '__all__'

    def create(self, validated_data):
        alumni = Alumni.objects.create(name=validated_data.get('name'),
                                       roll_no=validated_data.get('roll_no'),
                                       program=validated_data.get('program'),
                                       image=im_to_base64(
                                           validated_data.get('image')),
                                       date=validated_data.get('date'),
                                       year=validated_data.get('year'))
        return alumni


class MSSerializer(serializers.ModelSerializer):
    class Meta:
        model = MS
        fields = '__all__'

    def create(self, validated_data):
        ms = MS.objects.create(name=validated_data.get('name'),
                                       roll_no=validated_data.get('roll_no'),
                                    year=validated_data.get('year'),
                                       image=im_to_base64(
                                           validated_data.get('image'))
                                       )

        return ms
