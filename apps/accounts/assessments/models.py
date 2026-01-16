from django.db import models
from apps.templates.models import Template
from apps.vendors.models import Vendor

STATUS_CHOICES = (
    ('assigned', 'Assigned'),
    ('in_progress', 'In Progress'),
    ('submitted', 'Submitted'),
    ('reviewed', 'Reviewed'),
)

class Assessment(models.Model):
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='assigned')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

