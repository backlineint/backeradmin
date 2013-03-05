from django.db import models
from django.contrib.auth.models import User
#from django.core.serializers.python import Serializer

class Issue(models.Model):
    issue_id = models.IntegerField()
    external_issue_id = models.IntegerField()
    publish_time = models.DateTimeField('date published')
    description = models.CharField(max_length=200)
    def __unicode__(self):
        return self.description

class Entitlement(models.Model):
    user = models.ForeignKey(User)
    issue = models.ForeignKey(Issue)
