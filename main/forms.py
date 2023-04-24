from .models import AddUser
from django.forms import TextInput, ModelForm


class AddUserForm(ModelForm):
    class Meta:
        model = AddUser
        fields = ['title', 'name', 'phone']
        widgets = {
            "title": TextInput(attrs={
                'class': "form-control",
                'placeholder': "First Name"
            }),
            "name": TextInput(attrs={
                'class': "form-control",
                'placeholder': "Last Name"
            }),
            "phone": TextInput(attrs={
                'class': "form-control",
                'placeholder': "Phone Number"
            })
        }
