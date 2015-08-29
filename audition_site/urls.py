"""audition_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
#from .views import home, home_files, DancerSignUpView, dancerId
from . import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home, name='home'),
    url(r'^fail/$', views.fail, name='fail'),
    url(r'^signup/', views.DancerSignUpView.as_view()),
    url(r'^all/', views.all),
    url(r'^searchById/$', views.searchById),
    url(r'^searchByName/$', views.searchByName),
    url(r'^conflicts/', views.RandomizeView.as_view()),
    url(r'^randomize/', views.hidden_randomize_form_handler),
    url(r'^newcastinggroup/', views.CastingGroupFormView.as_view()),
    url(r'^(?P<filename>(robots.txt)|(humans.txt))$',
    views.home_files, name='home-files'),
    # url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    # url(r'^accounts/', include('allauth.urls')),
    url(r'^team/', views.team),
    # url(r'^dancer/', DancerIdView.as_view()),
    url(r'^successsignup/(?P<id>[0-9]+)/$', views.dancerId),
    url(r'^all_dancers/', views.allDancers),
    url(r'^dancer/(?P<dancerId>[0-9]+)/$', views.DancerProfileView.as_view()),
    # url(r'^dancer/randomize/$', views.hidden_randomize_form_handler),
    url(r'^dancer/add_to_team/(?P<dancerId>[0-9]+)/$', views.hidden_add_form_handler),
    url(r'^dancer/remove_from_team/(?P<dancerId>[0-9]+)/$', views.hidden_remove_form_handler),
    url(r'^teams/(?P<teamId>[0-9]+)/$', views.teamProfile),
    url(r'^castinggroup/(?P<groupId>[0-9]+)/$', views.castingGroupProfile),
    url(r'^successcastinggroup/(?P<id>[0-9]+)/$', views.castingGroupId),
        # url(r'^blog/page(?P<num>[0-9]+)/$', views.page),


]

urlpatterns += i18n_patterns(
    url(r'^$', views.home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
)