from django.db.models import Q
from django.views.generic import ListView

from main.models import Post


class Search(ListView):
    template_name = 'search/search_list.html'
    paginate_by = 10
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(Q(title__icontains=self.request.GET.get('s'), is_published=True) |
                                   Q(content__icontains=self.request.GET.get('s'), is_published=True))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s'] = f"s={self.request.GET.get('s')}&"
        return context
