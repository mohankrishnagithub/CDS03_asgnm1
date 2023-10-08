from django.db import models

# Create your models here.

class Tasks(models.Model):
    Title = models.TextField()
    Completed = models.BooleanField(default=False, blank=True, null=True)

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def __str__(self):
        return self.Title

