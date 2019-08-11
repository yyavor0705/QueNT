from django.conf.urls import url
from django.urls import path
from .views import index, company_page

urlpatterns = [
    url(r'^$', index),
    path('company/<int:id>', company_page, name='company-page'),
]
