from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

PEOPLE_TYPES = [
    ("Student", "I am a Student"),
    ("Teacher", "I am a Teacher"),
    ("Parent", "I am a Parent"),
]


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Question(models.Model):
    problem = models.TextField(max_length=100)
    tag = models.CharField(
        max_length=20, choices=PEOPLE_TYPES, default="Student")

    def __str__(self) -> str:
        return self.problem


class WebResource(models.Model):
    Name = models.CharField(max_length=200)
    Summary = models.TextField()
    link = models.CharField(max_length=500)
    question = models.ForeignKey(
        to=Question, on_delete=models.CASCADE, null=True)
    tag = models.CharField(
        max_length=20, choices=PEOPLE_TYPES, default="Parent")

    def __str__(self) -> str:
        return f"{self.Name}"
