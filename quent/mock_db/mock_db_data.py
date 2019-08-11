import os
import csv
import sys
import random
import django
from django.utils import timezone

sys.path.append('quent')
os.environ['DJANGO_SETTINGS_MODULE'] = 'quent.settings'
django.setup()

from djUI.models import Company, Worker, JobType


def mock_companies_and_job_types():
    Company.objects.all().delete()
    JobType.objects.all().delete()
    company_name = 0
    company_email = 1
    company_address = 2
    with open("company.csv") as comp_file, open("job_type.csv") as job_type_file, open("worker.csv") as worker_file:
        companies_list = csv.reader(comp_file, delimiter=',')
        job_types_list = list(csv.reader(job_type_file, delimiter=','))
        workers_list = list(csv.reader(worker_file, delimiter=','))
        for company in companies_list:
            new_company = Company.objects.get_or_create(email=company[company_email], name=company[company_name],
                                                        address=company[company_address])[0]
            for _ in range(0, random.randrange(2, 5)):
                job = random.choice(job_types_list)
                JobType.objects.create(title=job[0], description=job[1],
                                       duration=timezone.timedelta(minutes=int(job[2])), company=new_company)


def mock_workers():
    Worker.objects.all().delete()
    companies = Company.objects.all()
    with open("worker.csv") as csv_file:
        workers_csv_list = list(csv.reader(csv_file, delimiter=','))
        for company in companies:
            available_job_types = JobType.objects.filter(company=company)
            for _ in range(0, random.randrange(2, 5)):
                worker = workers_csv_list.pop()
                amount_of_job_types_worker_can_do = random.randrange(1, len(available_job_types))
                new_worker = Worker.objects.create(name=worker[0], email=worker[1],
                                                   company=company)
                available_job_types_list = list(available_job_types)
                for _ in range(0, amount_of_job_types_worker_can_do):
                    job_type = random.choice(available_job_types_list)
                    new_worker.job_type.add(job_type)
                    available_job_types_list.remove(job_type)


if __name__ == "__main__":
    print("Data population started ...")
    mock_companies_and_job_types()
    mock_workers()
    print("Data population completed.")
