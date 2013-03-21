from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:

#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('swift_meta.views',
    # Examples:
    # url(r'^$', 'test.views.home', name='home'),
    # url(r'^test/', include('test.ui.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'index'),
    url(r'index', 'index'),
    url(r'show','display_meta'),
)
