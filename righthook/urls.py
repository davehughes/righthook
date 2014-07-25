from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'', 'righthook.views.receive_hook', name='receive-hook'),
    )
