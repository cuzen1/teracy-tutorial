"""
common settings for urls
"""

from django.conf.urls import patterns, include, url  # noqa


urlpatterns = patterns(
    '',
    url(r'^polls/', include('apps.polls.urls')),
    # Examples:
    # url(r'^$', 'teracy.views.home', name='home'),
    # url(r'^teracy/', include('teracy.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
)
