from django.contrib import admin
from .models import Company, Worker, JobType, ScheduledJob

admin.site.register(Company)
admin.site.register(Worker)
admin.site.register(JobType)
admin.site.register(ScheduledJob)
