from django.conf.urls import patterns, include, url

from django.contrib import admin
from myapp.views import search_form, search,weatherDataDisplay,\
                              weatherDataStore,register,welcomeScreen
from django.contrib.auth.views import login, logout
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^myapp/', include('myapp.urls')),
    url(r'^$', welcomeScreen),
    url(r'^search-form/$',search_form),
    url(r'^search/$',search),
    url(r'^add_record/$',weatherDataDisplay),
    url(r'^add_wdata/$',weatherDataStore),
    url(r'^accounts/login/$',login),
    url(r'^accounts/logout/$',logout),
    url(r'^accounts/register/$',register),
    url(r'^accounts/profile/$',welcomeScreen),
)
