from django.forms import ModelForm

from pollution.models import PollutionSource


class PollutionSourceForm(ModelForm):
    class Meta:
        model = PollutionSource
        fields = ['description', 'address']
