from django.db import models
from .custom_duration import Duration
from django.contrib.auth.models import AbstractUser


class Company(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    logo = models.FileField(blank=True)

    class Meta:
        verbose_name = "Company"

    def __str__(self):
        return "{} {}".format(self.name, self.address)


class JobType(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    duration = Duration()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Job type"

    def __str__(self):
        return "{} ({})".format(self.title, self.company)


class UserProfile(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_worker = models.BooleanField(default=False)

    class Meta:
        verbose_name = "User profile"

    def __str__(self):
        return self.username


class Worker(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    photo = models.FileField(blank=True)
    job_types = models.ManyToManyField(JobType)

    class Meta:
        verbose_name = "Worker"

    def __str__(self):
        return self.user_profile.username


class ScheduledJob(models.Model):
    start_date_time = models.DateTimeField()
    job_type = models.OneToOneField(JobType, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Scheduled job"

    def __str__(self):
        return "{} ({} - {})".format(self.job_type.title, self.worker, self.start_date_time)
