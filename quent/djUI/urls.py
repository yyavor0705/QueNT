from django.urls import path, include
from .views import index, company_page, company_add, user_add, logout_view, login_view, worker_add, \
    company_schedules_view


user_url = [
    #path('<int:id>'),
    path('add/', user_add, name="user-add"),
    #path('delete/<int:id>', worker_add, "user-delete"),
    #path('update/<int:id>', worker_add, "user-update"),
]


worker_url = [
    #path('<int:id>'),
    path('add', worker_add, name="worker-add"),
    #path('delete/<int:id>', worker_add, "worker-delete"),
    #path('update/<int:id>', worker_add, "worker-update"),
]


company_url = [
    path('<int:id>', company_page, name="company-page"),
    path("<int:company_id>/schedules/<int:year>/<int:month>/<int:day>", company_schedules_view),
    path('add', company_add, name="company-add"),
    #path('delete/<int:id>', worker_add, "company-delete"),
    #path('update/<int:id>', worker_add, "company-update"),
    path('<int:company_id>/worker/', include(worker_url))

]


urlpatterns = [
    path('', index, name='index'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('company/', include(company_url)),
    path('user/', include(user_url)),
]
