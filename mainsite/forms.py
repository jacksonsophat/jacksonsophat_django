from django import forms
# from django.forms import ModelForm
from .models import AmazonPriceTracking, ContactUs

class AmazonForm(forms.ModelForm):
    class Meta:
        model = AmazonPriceTracking
        fields = "__all__"

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ContactUsForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'input-basic black'