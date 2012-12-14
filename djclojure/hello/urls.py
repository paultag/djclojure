from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'djclojure.hello.views.home', name='home'),
)

