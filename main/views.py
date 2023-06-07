from django.db.models import F
from django.views.generic import DetailView, ListView

from .models import Post, Tag


class FrontPage(ListView):
    model = Post
    template_name = 'main/frontpage.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(is_published=True)


class PostList(ListView):
    model = Post
    template_name = 'main/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(is_published=True)


class PostDetail(DetailView):
    model = Post
    template_name = 'main/post_detail.html'
    context_object_name = 'post_detail'
    slug_url_kwarg = 'slug'

    def get_success_url(self):
        return self.request.path

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context


class PostByTag(ListView):
    template_name = 'main/post_by_tag.html'
    paginate_by = 8
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs['slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Записи по тегу: ' + str(Tag.objects.get(slug=self.kwargs['slug']))
        return context
