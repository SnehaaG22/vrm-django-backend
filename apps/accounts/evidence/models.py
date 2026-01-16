from django.db import models
from apps.assessments.models import Assessment
from apps.templates.models import Question

class Evidence(models.Model):
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    file_url = models.CharField(max_length=500)
    expiry_date = models.DateField(null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
