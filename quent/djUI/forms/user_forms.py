from django import forms
from django.contrib.auth.forms import UserCreationForm

from djUI.models import UserProfile, Worker


class UserProfileForm(UserCreationForm):
    is_admin = forms.BooleanField(disabled=True)

    class Meta:
        model = UserProfile
        fields = UserCreationForm.Meta.fields

    def show_is_admin_field(self):
        self.fields["is_admin"].disabled = False


class WorkerForm(forms.ModelForm):

    class Meta:
        model = Worker
        fields = ["photo", "job_types"]
