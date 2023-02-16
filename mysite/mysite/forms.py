
from django import forms

from .models import User


class MyForm(forms.Form):
    name = forms.CharField(label="User name", max_length=40, initial="User name",
                           error_messages={'required': 'Please enter your'
                                                       ' available email'})
    email = forms.EmailField(initial="admin@admin.com", error_messages={
        'required': 'Please enter your available email'})
    password = forms.CharField(max_length=20, min_length=10,
                               required=False,
                               widget=forms.PasswordInput())
    age = forms.IntegerField(required=False, initial="18",
                             help_text="Enter your current age")
    gender = forms.ChoiceField(required=False,
                               choices=[("1", "man"), ("2", "woman")])

class FormFromModel(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'




