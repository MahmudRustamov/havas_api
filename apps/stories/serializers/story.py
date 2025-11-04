from rest_framework import serializers
from apps.stories.models import (
    StoriesModel, StoriesSlide, StoriesSurvey,
    SurveyQuestion, SurveyAnswer
)

# Survey javoblari serializer
class SurveyAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyAnswer
        fields = ['id', 'text', 'is_correct']


class SurveyQuestionSerializer(serializers.ModelSerializer):
    answers = SurveyAnswerSerializer(many=True, read_only=True)

    class Meta:
        model = SurveyQuestion
        fields = ['id', 'text', 'order', 'multiple_choice', 'answers']

# Story survey serializer
class StoriesSurveySerializer(serializers.ModelSerializer):
    questions = SurveyQuestionSerializer(many=True, read_only=True)

    class Meta:
        model = StoriesSurvey
        fields = ['id', 'title', 'description', 'questions']

# Story slide serializer
class StoriesSlideSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoriesSlide
        fields = ['id', 'title', 'text', 'image', 'video_url', 'order', 'show_progress']

# Story serializer
class StoriesModelSerializer(serializers.ModelSerializer):
    slides = StoriesSlideSerializer(many=True, read_only=True)
    survey = StoriesSurveySerializer(read_only=True)

    class Meta:
        model = StoriesModel
        fields = ['id', 'title', 'slug', 'description', 'image', 'video_url', 'is_active', 'start_date', 'end_date', 'slides', 'survey']

