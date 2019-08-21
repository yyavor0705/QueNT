from django.contrib.auth.forms import UserCreationForm
from djUI.models import UserProfile


class UserProfileForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = UserCreationForm.Meta.fields
