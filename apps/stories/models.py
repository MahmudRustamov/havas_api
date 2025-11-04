from django.db import models
from django.contrib.auth import get_user_model
from apps.shared.models import BaseModel

User = get_user_model()


class StoriesModel(BaseModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='stories/', blank=True, null=True)  # Rasm
    video_url = models.URLField(blank=True, null=True)  # Video link
    is_active = models.BooleanField(default=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title


class StoriesSlide(BaseModel):
    story = models.ForeignKey(StoriesModel, related_name='slides', on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)
    title = models.CharField(max_length=255, blank=True)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='stories/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    show_progress = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title



class StoriesSurvey(BaseModel):
    story = models.OneToOneField(StoriesModel, related_name='survey', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class SurveyQuestion(BaseModel):
    survey = models.ForeignKey(StoriesSurvey, related_name='questions', on_delete=models.CASCADE)
    text = models.TextField()
    order = models.PositiveIntegerField(default=0)
    multiple_choice = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class SurveyAnswer(BaseModel):
    question = models.ForeignKey(SurveyQuestion, related_name='answers', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class UserStoryProgress(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='story_progress')
    story = models.ForeignKey(StoriesModel, on_delete=models.CASCADE, related_name='user_progress')
    is_completed = models.BooleanField(default=False)
    last_slide = models.PositiveIntegerField(default=0)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.story.title}"


class UserSurveyAnswer(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='survey_answers')
    question = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE, related_name='user_answers')
    selected_answers = models.ManyToManyField(SurveyAnswer, related_name='selected_by_users')
    answered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.question.text}"
