from django.conf.urls import url
from django.urls import path
from tempapp import views

app_name = 'tempapp'

urlpatterns = [
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^other/$',views.other,name='other'),
]
