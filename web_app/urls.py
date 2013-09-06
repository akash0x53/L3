from django.conf.urls import patterns, include, url
import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$',views.welcome),
                       url('^submit/$',views.get_url),
                       url('^store/$',views.store_db),
    # Examples:
    # url(r'^$', 'web_app.views.home', name='home'),
    # url(r'^web_app/', include('web_app.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
