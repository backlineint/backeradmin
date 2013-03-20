from django.contrib import admin
from entitlements.models import Issue, Entitlement

class IssueAdmin(admin.ModelAdmin):
    list_display = ('description', 'issue_id', 'external_issue_id', 'publish_time')
class EntitlementAdmin(admin.ModelAdmin):
    raw_id_fields = ('user',)
    list_display = ('user', 'issue')

admin.site.register(Issue, IssueAdmin)
admin.site.register(Entitlement, EntitlementAdmin)
