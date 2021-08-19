from django import forms
from .models import feedback

class feedbackForm(forms.ModelForm):
    class Meta:
        model = feedback
        fields = ['fullName', 'emailId', 'phoneNumber', 'message', 'subject']
