from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
    url(r'^$', 'imgdb.views.home', name='home'),
                       url(r'^user_center/', 'utils.views.user_center', name='users_center'),
                       url('accounts/', include('users.urls')),
                       url('grappelli/', include('grappelli.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       )
