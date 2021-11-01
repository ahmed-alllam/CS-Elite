from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from articles.forms import AddCommentForm
from django.contrib.auth.mixins import LoginRequiredMixin

class DetailedArticleView(TemplateView):
    template_name = 'article.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ArticlesByTagView(TemplateView):
    template_name = 'articles.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CommentCreateView(LoginRequiredMixin, CreateView):
    http_method_names = ['post']
    form_name = AddCommentForm

    def get_form_kwargs(self):
        kwargs = super(CommentCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        kwargs['article'] = self.kwargs.get("slug")
        return kwargs

    def get_success_url(self):
        return '/articles/' + self.kwargs.get("slug") + '/'
