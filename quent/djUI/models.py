from django.db import models


class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Worker(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class JobType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    description = models.TextField()
    duration = models.DurationField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)


class ScheduledJob(models.Model):
    date_time = models.DateTimeField()
    job_type = models.OneToOneField(JobType, on_delete=models.CASCADE, null=True)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, null=True)
