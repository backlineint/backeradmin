from django.contrib import admin
from entitlements.models import Issue

class IssueAdmin(admin.ModelAdmin):
    list_display = ('description', 'issue_id', 'external_issue_id', 'publish_time')

admin.site.register(Issue, IssueAdmin)
