from django.urls import path
from apps.stories.views.story_view import (
    StoryListCreateAPIView, StoryRetrieveUpdateDestroyAPIView,
    SlideCreateAPIView, SlideRetrieveUpdateDestroyAPIView,
    SurveyCreateAPIView, SurveyRetrieveUpdateDestroyAPIView,
    SurveyQuestionCreateAPIView, SurveyQuestionRetrieveUpdateDestroyAPIView,
    SurveyAnswerCreateAPIView, SurveyAnswerRetrieveUpdateDestroyAPIView
)

app_name = 'stories'
urlpatterns = [
    # Story
    path('', StoryListCreateAPIView.as_view(), name='stories-list-create'),
    path('<int:id>/', StoryRetrieveUpdateDestroyAPIView.as_view(), name='stories-detail'),

    # Slide
    path('slides/', SlideCreateAPIView.as_view(), name='slides-create'),
    path('slides/<int:id>/', SlideRetrieveUpdateDestroyAPIView.as_view(), name='slides-detail'),

    # Survey
    path('surveys/', SurveyCreateAPIView.as_view(), name='survey-create'),
    path('surveys/<int:id>/', SurveyRetrieveUpdateDestroyAPIView.as_view(), name='survey-detail'),

    # Question
    path('questions/', SurveyQuestionCreateAPIView.as_view(), name='question-create'),
    path('questions/<int:id>/', SurveyQuestionRetrieveUpdateDestroyAPIView.as_view(), name='question-detail'),

    # Answer
    path('answers/', SurveyAnswerCreateAPIView.as_view(), name='answer-create'),
    path('answers/<int:id>/', SurveyAnswerRetrieveUpdateDestroyAPIView.as_view(), name='answer-detail'),
]
