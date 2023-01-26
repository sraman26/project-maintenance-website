from django.db import models
from projects.models import Project
from django.conf import settings

# Create your models here.


class Task(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    due_date = models.DateTimeField()
    project = models.ForeignKey(
        Project,
        related_name="tasks",
        on_delete=models.CASCADE,
    )
    assignee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        related_name="tasks",
        on_delete=models.CASCADE,
    )
