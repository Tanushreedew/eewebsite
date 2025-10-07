from rest_framework import serializers
from .models import Announcements

class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcements
        fields = '__all__'
        
    def create(self,validated_data):
        Announcement = Announcements.objects.create(title=validated_data.get('title'),
                                                    description=validated_data.get('description'),
                                                    link=validated_data.get('link'))
        return Announcement
    
    def update(self,validated_data):
        try:
            Announcement = Announcements.objects.get(id=validated_data['announcements_id'])
        except Announcement.DoesNotExist:
            raise ValueError("Announcement doesn't exist with given id")
        if validated_data.get('title'):
            Announcement.title = validated_data.get('title')
        if validated_data.get('description'):
            Announcement.description = validated_data.get('description')
        if validated_data.get('link'):
            Announcement.link = validated_data.get('link')
        Announcement.save(update_fields=['title','description','link'])
        return Announcement
    
