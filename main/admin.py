from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin

from .models import Post, Tag


class PostAdminForm(forms.ModelForm):
    """Форма для контента ckeditor"""
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'updated_at', 'created_at', 'views')
    prepopulated_fields = {'slug': ('title',)}
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    form = PostAdminForm
    list_filter = ('is_published', 'tags')
    readonly_fields = ('views', 'created_at', 'updated_at')


class TagAdmin(admin.ModelAdmin):
    """Для тэгов"""
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)

admin.site.site_title = 'Управление публикациями'
admin.site.site_header = 'Управление публикациями'
