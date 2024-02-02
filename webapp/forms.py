from django.forms import ModelForm
from .models import Laptop



class UpdateForm(ModelForm):
    class Meta:
        model = Laptop
        fields = '__all__'


class AddForm(ModelForm):
    class Meta:
        model = Laptop
        fields = ['images', 'brand', 'model', 'processor', 'ram', 'storage', 'graphics', 'price']

