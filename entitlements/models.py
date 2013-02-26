from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Issue(models.Model):
    issue_id = models.IntegerField()
    external_issue_id = models.IntegerField()
    publish_time = models.DateTimeField('date published')
    description = models.CharField(max_length=200)
