from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from .models import Company, Worker, JobType, ScheduledJob
from .forms.company_forms import NewCompany


def index(request):
    companies = Company.objects.all()
    return render(request, "main.html", context={
        "companies": companies
    })


def company_page(request, id):
    company = Company.objects.filter(id=id)[0]
    return render(request, "company.html", context={
        "company": company
    })


def company_add(request):
    new_company_model_form = NewCompany()
    if request.method == 'POST':
        new_company_model_form = NewCompany(request.POST)

        if new_company_model_form.is_valid():
            new_company_model_form.save()
            return company_page(request, new_company_model_form.instance.id)
    return render(request, "new_company.html", context={
        "form": new_company_model_form
    })


def login_view(request):
    if request.method == "POST":
        user_name = request.POST.get("user_name")
        user_password = request.POST.get("user_password")
        user = authenticate(username=user_name, password=user_password)
        if user:
            if user.is_active:
                login(request, user)
    return HttpResponseRedirect(request.path)


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")


def user_add(request):
    return HttpResponseRedirect(request.path_info)
