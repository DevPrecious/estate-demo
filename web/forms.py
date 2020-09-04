from django.forms import ModelForm
from .models import Requests

class RequestForm(ModelForm):
	class Meta:
		model = Requests
		fields = '__all__'