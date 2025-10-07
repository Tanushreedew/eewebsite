from rest_framework import serializers
from .models import Events


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'

    def create(self, validated_data):
        event = Events.objects.create(title=validated_data.get('title'),
                                      description=validated_data.get(
            'description'),
            date=validated_data.get('date'),
            month=validated_data.get('month'),
            day=validated_data.get('day'),
            image=validated_data.get('image'),
            link=validated_data.get('link'),
            time=validated_data.get('time'))
        return event

    def update(self, validated_data):
        try:
            event = Events.objects.get(
                id=validated_data['events_id'])
        except event.DoesNotExist:
            raise ValueError("Event doesn't exist with given id")
        if validated_data.get('title'):
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
