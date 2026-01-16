from django.contrib.auth.models import AbstractUser
from django.db import models
from apps.orgs.models import Organization

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('reviewer', 'Reviewer'),
        ('requester', 'Requester'),
        ('vendor', 'Vendor'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    org = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True, blank=True)
