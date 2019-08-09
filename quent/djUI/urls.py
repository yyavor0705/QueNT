from django.conf.urls import url
from first_app.views import index

urlpatterns = [
    url(r'^$', index, name='index'),
]
