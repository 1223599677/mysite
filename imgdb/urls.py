from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'imgdb.views.home', name='home'),

    url(r'^user_center/', 'utils.views.user_center', name='user-center'),

    url(r'^genome_center/', 'utils.views.genome_center', name='genome-center'),
    url(r'^genome_upload/', 'utils.views.genome_upload', name='genome-upload'),
    url(r'^genome_browser/', 'utils.views.genome_browser', name='genome-browser'),
    url(r'^change/private/genome/$', 'utils.views.change_private_genome',
        name='change-private-genome'),

    url(r'^search/sequence_info/$', 'utils.views.search_sequence_info',
        name='search-sequence-info'),

    url('accounts/', include('users.urls')),
    url('grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
