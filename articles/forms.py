from django import forms
from django.core.exceptions import ValidationError
from django.forms import models as forms
from articles.models import Article, User
from . import models

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['text', 'user', 'article']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        article = kwargs.pop('article', None)
        
        super(AddCommentForm, self).__init__(*args, **kwargs)

        if user:
            self.data.update({'user': user})
        
        if article:
            self.data.update({'article': article})
 
    def clean_user(self):
        user = self.cleaned_data.get('user', None)

        if not (user and User.objects.exists(pk=user.pk)):
            raise ValidationError("User Doesn't Exist")

        return user

    def clean_article(self):
        article = self.cleaned_data.get('article', None)

        if article:
            try:
                return Article.objects.get(slug=article)
            except Article.DoesNotExist:
                pass

        raise ValidationError("Article Doesn't Exist")
