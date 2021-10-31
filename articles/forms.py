from django import forms
from django.forms import models as forms
import models

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['text']
