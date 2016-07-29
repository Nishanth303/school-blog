from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    url(r'^about/$', views.about, name='about'),
    url(r'^event/$', views.event, name='event'),
    url(r'^calendar/$', views.calendar, name='calendar'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^class_a/$', views.class_a, name='class_a'),
    url(r'^login/$', views.login, name='login'),
    url(r'^login_submit/$', views.login_submit, name='login_submit'),
    url(r'^class_info/$', views.class_info, name='class_info'),
]
