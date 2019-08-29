from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, logout

from .models import Company, Worker, JobType, ScheduledJob, UserProfile
from .forms.company_forms import NewCompany
from .forms.user_forms import UserProfileForm, WorkerForm
from .authentication.validator import company_admin_required


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


@login_required
def company_add(request):
    new_company_model_form = NewCompany()
    if request.method == 'POST':
        new_company_model_form = NewCompany(request.POST)

        if new_company_model_form.is_valid():
            new_company = new_company_model_form.save()
            user = request.user
            user.is_admin = True
            user.is_worker = True
            user.save()
            Worker.objects.create(user_profile=user, company=new_company)
            return HttpResponseRedirect("{}".format(new_company_model_form.instance.id))
    return render(request, "new_company.html", context={
        "form": new_company_model_form
    })


def login_view(request):
    next_page = request.GET.get("next")
    if request.method == "POST":
        user_name = request.POST.get("user_name")
        user_password = request.POST.get("user_password")
        user = authenticate(username=user_name, password=user_password)
        if user:
            if user.is_active:
                login(request, user)
    return HttpResponseRedirect(next_page)


@login_required
def logout_view(request):
    next_page = request.GET.get("next")
    logout(request)
    return HttpResponseRedirect(next_page)


def user_add(request):
    new_user_form = UserProfileForm()
    if request.method == "POST":
        new_user_form = UserProfileForm(request.POST)
        if new_user_form.is_valid():
            new_user_form.save()
            new_user = authenticate(username=new_user_form.cleaned_data.get("username"),
                                    password=new_user_form.cleaned_data.get("password1"))
            login(request, new_user)
            return HttpResponseRedirect("/")
    return render(request, "user_registration.html", context={
        "user_profile_form": new_user_form
    })


@user_passes_test(lambda user: user.is_admin, login_url="/")
def worker_add(request, company_id):
    new_user_form = UserProfileForm()
    new_user_form.show_is_admin_field()
    new_worker_form = WorkerForm()
    if request.method == "POST":
        new_user_form = UserProfileForm(request.POST)
        if new_user_form.is_valid() and new_worker_form.is_valid():
            new_user = new_user_form.save(commit=False)
            new_user.is_admin = True
            new_user.save()

            company = Company.objects.filter(pk=company_id)[0]
            new_worker = new_worker_form.save(commit=False)
            new_worker.user_profile = new_user
            new_worker.company = company
            new_worker.save()

            return HttpResponseRedirect("/")
    return render(request, "worker_registration.html", context={
        "user_profile_form": new_user_form,
        "worker_form": new_worker_form
    })

