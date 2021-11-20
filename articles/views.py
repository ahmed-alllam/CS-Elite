from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from articles import models
from articles.forms import AddCommentForm
from django.contrib.auth.mixins import LoginRequiredMixin

class DetailedArticleView(DetailView):
    template_name = 'article_detail.html'
    model = models.Article
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = models.Category.objects.filter()
        context['top_categories'] = models.Category.objects.filter()[:5]

        article = context['object']
        article.views_count += 1
        article.save()

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
