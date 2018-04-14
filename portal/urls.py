from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^add_new$', views.add_new, name='add_new'),
    url(r'^show_all$', views.show_all, name='show_all'),
    url(r'^edit_point/(?P<id>[0-9]+)$', views.edit_point, name='edit_point'),
]