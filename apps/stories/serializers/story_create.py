from rest_framework import serializers

from apps.stories.models import StoriesSlide, StoriesModel, StoriesSurvey, SurveyQuestion, SurveyAnswer


class StoriesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoriesModel
        fields = ['title', 'slug', 'description', 'image', 'video_url', 'is_active', 'start_date', 'end_date']

class StoriesSlideCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoriesSlide
        fields = ['story', 'title', 'text', 'image', 'video_url', 'order', 'show_progress']

class StoriesSurveyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoriesSurvey
        fields = ['story', 'title', 'description']

class SurveyQuestionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyQuestion
        fields = ['survey', 'text', 'order', 'multiple_choice']

class SurveyAnswerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyAnswer
        fields = ['question', 'text', 'is_correct']
