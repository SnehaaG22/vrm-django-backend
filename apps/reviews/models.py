from django.db import models
from apps.assessments.models import Assessment
class Review(models.Model):
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    reviewer_notes = models.TextField()
    reviewed_at = models.DateTimeField(auto_now_add=True)

