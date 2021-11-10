from django.views.generic.base import TemplateView
from articles import models
class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = models.Article.objects.filter()
        context['categories'] = models.Category.objects.filter()
        context['top_categories'] = models.Category.objects.filter()[0:5]
        return context

class ArticlesByCategory(TemplateView):
    template_name = 'articles_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
