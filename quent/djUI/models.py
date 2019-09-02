from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser

from .custom_duration import Duration


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
    hex_color = models.CharField(max_length=6, null=True)
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
    job_type = models.ForeignKey(JobType, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Scheduled job"

    def __str__(self):
        return "{} ({} - {})".format(self.job_type.title, self.worker, self.start_date_time)

    def clean(self):
        if self.__time_overlaps():
            raise ValidationError("This time isn't available for scheduling.")

    def __time_overlaps(self):
        existing_schedules = ScheduledJob.objects.filter(worker=self.worker,
                                                         start_date_time__year=self.start_date_time.year,
                                                         start_date_time__month=self.start_date_time.month,
                                                         start_date_time__day=self.start_date_time.day)
        new_schedule_start_time = self.start_date_time.time()
        new_schedule_end_time = (self.start_date_time + self.job_type.duration).time()

        for existing_schedule in existing_schedules:
            existing_schedule_start = existing_schedule.start_date_time.time()
            existing_schedule_end = (existing_schedule.start_date_time + existing_schedule.job_type.duration).time()
            overlaps = existing_schedule_start <= new_schedule_start_time < existing_schedule_end or \
                new_schedule_start_time <= existing_schedule_start < new_schedule_end_time or \
                (existing_schedule_start == new_schedule_start_time and
                 existing_schedule_end == new_schedule_end_time)
            if overlaps:
                return True

        return False

