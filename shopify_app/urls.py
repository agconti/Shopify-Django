from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
        url(r'^$', 'shopify_app.views.login', name="login"),
        url(r'^authenticate/$', 'shopify_app.views.authenticate', name='authenticate'),
        url(r'^finalize/$', 'shopify_app.views.finalize', name='finalize'),
        url(r'^logout/$', 'shopify_app.views.logout', name='logout'),
)
