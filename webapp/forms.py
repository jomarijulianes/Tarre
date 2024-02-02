from django.forms import ModelForm
from .models import Laptop, Classification



class UpdateForm(ModelForm):
    class Meta:
        model = Laptop
        fields = '__all__'


class AddForm(ModelForm):
    class Meta:
        model = Laptop
        fields = ['images', 'brand', 'model', 'processor', 'ram', 'storage', 'graphics', 'price']

    def save(self, commit=True, *args, **kwargs):
        instance = super(AddForm, self).save(commit=False, *args, **kwargs)
        instance.save()

        # Create Classification
        if instance.price and int(instance.price) <= 15000:
            classification_type = 'Budget-Friendly'
        elif 15000 < int(instance.price) <= 30000:
            classification_type = 'Mid-Range'
        else:
            classification_type = 'High-End'

        Classification.objects.create(
            laptop=instance,
            classification_type=classification_type
        )

        return instance