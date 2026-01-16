from django.db import models
from apps.assessments.models import Assessment

class Renewal(models.Model):
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    due_date = models.DateField()
    renewed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

