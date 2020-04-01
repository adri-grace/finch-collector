from django.forms import ModelForm
from .models import Siting

class SitingForm(ModelForm):
    class Meta:
        model = Siting
        fields = ['date', 'sex']