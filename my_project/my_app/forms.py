from django import forms
from .models import TodoItems

class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoItems
        fields = '__all__'
        widgets = {
            'text': forms.TextInput(attrs={'placeholder': 'Enter your new TODO'}),
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name'}),
        }

class DeleteTodoForm(forms.Form):
    confirm = forms.BooleanField(required=True, label="Confirm Deletion")

# class EditTodoForm(forms.Form):
#     confirm = forms.BooleanField(required=True, label="confirm Edit")
