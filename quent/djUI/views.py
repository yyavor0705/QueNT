from django.shortcuts import render
from .models import Company, Worker, JobType, ScheduledJob


# Create your views here.
def index(request):
    companies = Company.objects.all()
    return render(request, "main.html", context={
        "companies": companies
    })


def company_page(request, id):
    company = Company.objects.filter(id=id)[0]
    print(company.name)
    return render(request, "company.html", context={
        "comp": company
    })