from apps.templates.models import *
class Template(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    version = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

class Section(models.Model):
    template = models.ForeignKey(Template, on_delete=models.CASCADE, related_name='sections')
    name = models.CharField(max_length=255)
    weight = models.FloatField(default=1.0)

class Question(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    weight = models.FloatField(default=1.0)
    red_flag = models.BooleanField(default=False)
    mandatory_evidence = models.BooleanField(default=False)
