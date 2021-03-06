from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from api import v1_api

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', login, name='login', kwargs={'template_name': 'login.html'}),
    url(r'^logout/$', logout, name='logout', kwargs={'template_name': 'logged_out.html'}),
    url(r'^explorer/', include('explorer.urls')),  # django-sql-explorer
]

# Additional URLS for development/debug.
if settings.DEBUG:
    # Add in Debug Toolbar URLs.
    import debug_toolbar
    urlpatterns.append(url(r'^__debug__/', include(debug_toolbar.urls)))

# PRS project URLs - must be placed after the debug_toolbar URLs.
urlpatterns += [
    url(r'^api/', include(v1_api.urls)),  # All API views are registered in api.py
    url(r'^reports/', include('reports.urls')),
    url(r'^', include('referral.urls')),
]
