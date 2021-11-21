from django.views.generic.list import ListView
from articles import models
from videos.models import YoutubeVideo
class HomeView(ListView):
    template_name = 'index.html'
    model = models.Article
    paginate_by = 20
    context_object_name = 'articles'
    pages_range = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = models.Category.objects.filter()
        context['top_categories'] = models.Category.objects.filter()[:5]
        context['top_articles'] = models.Article.objects.order_by('-views_count')[:5]
        context['videos'] = YoutubeVideo.objects.filter()[:5]
        context.update(self.get_paginator_context(context.get('page_obj')))

        return context
    
    def get_paginator_context(self, page_obj):
        return {
            'previous_pages_range': range(max(1, page_obj.number - self.pages_range), 
                                    page_obj.number),
            'next_pages_range': range(page_obj.number + 1, 
                                    min(page_obj.paginator.num_pages + 1, 
                                        page_obj.number + self.pages_range + 1))
        }

class ArticlesByCategory(ListView):
    template_name = 'articles.html'
    model = models.Article
    paginate_by = 20
    context_object_name = 'articles'
    pages_range = 5

    def get_queryset(self):
        return super().get_queryset().filter(category__slug=self.kwargs.get('slug'))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = models.Category.objects.filter()
        context['top_categories'] = models.Category.objects.filter()[:5]
        context['category_title'] = models.Category.objects.get(slug=self.kwargs.get('slug')).title
        return context
