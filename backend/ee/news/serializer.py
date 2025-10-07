from rest_framework import serializers
from .models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

    def create(self, validated_data):
        news = News.objects.create(title=validated_data.get('title'),
                                    description=validated_data.get(
            'description'),
            date=validated_data.get('date'),
            month=validated_data.get('month'),
            day=validated_data.get('day'),
            link=validated_data.get('link'),
            time=validated_data.get('time'))
        return news 

    # def update(self, validated_data):
    #     try:
    #         news = News.objects.get(id=validated_data['news_id'])
    #     except news.DoesNotExist:
    #         raise ValueError('News with the given ID does not exist')
    #     if validated_data.get('title'):
    #         news.title = validated_data.get('title')
    #     if validated_data.get('description'):
    #         news.description = validated_data.get('description')
    #     if validated_data.get('date'):
    #         news.date = validated_data.get('date')
    #     if validated_data.get('link'):
    #         news.link = validated_data.get('link')
    #     news.save(update_fields=['title', 'description', 'date', 'link'])
    #     return news
