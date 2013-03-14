from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'backeradmin.views.home', name='home'),
    # url(r'^backeradmin/', include('backeradmin.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'backeradmin/login.html'}),
    url(r'^login/$', 'myaccount.views.custom_login', name='login'),
    url(r'^handler/$', 'myaccount.views.handler'),
    url(r'^entitlements/$', 'entitlements.views.get_entitlements'),
    url(r'^myaccount/$', 'myaccount.views.myaccount'),
    url(r'^myaccount_changed/$', 'myaccount.views.myaccount_changed'),
    url(r'^logout/$', 'myaccount.views.custom_logout'),
    url(r'^close/$', 'myaccount.views.close', name='close'),
    url(r'^publishissue/$', 'publishissue.views.publish_issue'),
    url(r'^downloadcomplete/$', 'downloadcomplete.views.download_complete'),
    url(r'^change/$', 'django.contrib.auth.views.password_change', {'post_change_redirect': '/myaccount_changed', 'template_name': 'registration/change.html'})
)
