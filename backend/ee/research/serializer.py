from rest_framework import serializers
from .models import Research, PGLabs, Papers, Projects, UGLabs


class ResearchSerializers(serializers.ModelSerializer):
    class Meta:
        model = Research
        fields = '__all__'

    def create(self, validated_data):
        research = Research.objects.create(specialization=validated_data.get('specialization'),
                                           person=validated_data.get('person'),
                                           name=validated_data.get('name'),
                                           description=validated_data.get(
                                               'description'),
                                           link=validated_data.get('link'))
        return research

    def update(self, validated_data):
        try:
            research = Research.objects.get(validated_data['research_id'])
        except research.DoesNotExist:
            raise ValueError('research with the following id does not exist')

        if validated_data.get('specialization'):
            research.specialization = validated_data.get('specialization')
        if validated_data.get('person'):
            research.person = validated_data.get('person')
        if validated_data.get('description'):
            research.description = validated_data.get('description')

        research.save(
            update_fields=['specialization', 'person', 'description'])
        return research


class PGLabsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PGLabs
        fields = '__all__'

    def create(self, validated_data):
        labs = PGLabs.objects.create(name=validated_data.get('name'),
                                     person=validated_data.get('person'),
                                     link=validated_data.get('link'),
                                     description=validated_data.get('description'),
                                     location=validated_data.get('location'),
                                     area=validated_data.get('area'),
                                     category=validated_data.get('category'),
                                     equipments=validated_data.get('equipments'),
                                     review=validated_data.get('review'),
                                     keywords=validated_data.get('keywords'),
                                     image=validated_data.get('image'),)
        return labs

    def update(self, validated_data):
        try:
            labs = PGLabs.objects.get(id=validated_data['labs_id'])
        except labs.DoesNotExist:
            raise ValueError('lab with the required id does not exist')

        if validated_data.get('name'):
            labs.name = validated_data.get('name')
        if validated_data.get('link'):
            labs.link = validated_data.get('link')
        if validated_data.get('person'):
            labs.person = validated_data.get('person')
        labs.save(update_fields=['name', 'person', 'link'])


class UGLabsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UGLabs
        fields = '__all__'
    
    def create(self,validated_data):
        ugLab = UGLabs.objects.create(name=validated_data.get('name'),
                                     experiments=validated_data.get('experiments'),
                                     equipments=validated_data.get('equipments'),
                                      image=validated_data.get('image'))
        return ugLab


class PapersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Papers
        fields = '__all__'

    def create(self, validated_data):
        Paper = Papers.objects.create(specialization=validated_data.get('specialization'),
                                      person=validated_data.get('person'),
                                      year=validated_data.get('year'))
        return Paper

    def update(self, validated_data):
        try:
            Paper = Papers.objects.get(validated_data['Papers_id'])
        except Paper.DoesNotExist:
            raise ValueError('Papers with the following id does not exist')

        if validated_data.get('specialization'):
            Paper.specialization = validated_data.get('specialization')
        if validated_data.get('person'):
            Paper.person = validated_data.get('person')
        if validated_data.get('year'):
            Paper.year = validated_data.get('year')

        Paper.save(
            update_fields=['specialization', 'person', 'year'])
        return Paper


class ProjectsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'

    def create(self, validated_data):
        Project = Projects.objects.create(title=validated_data.get('title'),
                                          worker=validated_data.get('worker'),
                                          funding=validated_data.get(
                                              'funding'),
                                          duration=validated_data.get(
                                              'duration'),
                                          project_type=validated_data.get('project_type'),)
        return Project

    def update(self, validated_data):
        try:
            Project = Projects.objects.get(validated_data['Projects_id'])
        except Project.DoesNotExist:
            raise ValueError('Projects with the following id does not exist')

        if validated_data.get('specialization'):
            Project.specialization = validated_data.get('specialization')
        if validated_data.get('person'):
            Project.person = validated_data.get('person')
        if validated_data.get('description'):
            Project.description = validated_data.get('description')

        Project.save(
            update_fields=['specialization', 'person', 'description'])
        return Project
