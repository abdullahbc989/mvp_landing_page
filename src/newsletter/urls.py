from django.conf.urls import url

from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'mvp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.home, name='home'),
    url(r'^contact/$', views.contact, name='contact'),
]
