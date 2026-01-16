from django.db import models
from apps.assessments.models import Assessment

class Remediation(models.Model):
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    description = models.TextField()
    due_date = models.DateField(null=True, blank=True)
    resolved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
