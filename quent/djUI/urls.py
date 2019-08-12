from django.urls import path
from .views import index, company_page, company_add

urlpatterns = [
    path('', index, name='index'),
    path('company/<int:id>', company_page, name='company-page'),
    path('company/add', company_add, name='company-add'),
]
