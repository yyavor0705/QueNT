from django.urls import path
from .views import index, company_page, company_add, user_add, logout_view, login_view

urlpatterns = [
    path('', index, name='index'),
    path('company/<int:id>', company_page, name='company-page'),
    path('company/add', company_add, name='company-add'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('user/add', user_add, name='register_user'),
]
