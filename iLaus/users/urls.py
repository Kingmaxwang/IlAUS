
from django.conf.urls import patterns, url, include

from . import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = [
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    url(r'^login/$', views.login_handler, name='login_review'),
]