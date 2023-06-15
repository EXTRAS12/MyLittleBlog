from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from modeltranslation.admin import TranslationAdmin

from .models import FlatPage, NewFlatpage, Post, Tag


class NewFlatpageInline(admin.StackedInline):
    model = NewFlatpage
    verbose_name = "Содержание"


class FlatPageNewAdmin(FlatPageAdmin, TranslationAdmin):
    inlines = [NewFlatpageInline]
    fieldsets = (
        (None, {'fields': ('url', 'title', 'sites')}),
        (('Advanced options'), {
            'fields': ('template_name',),
        }),
    )
    list_display = ('url', 'title')
    list_filter = ('sites', 'registration_required')
    search_fields = ('url', 'title')


class PostAdminForm(forms.ModelForm):
    """Форма для контента ckeditor"""
    content_ru = forms.CharField(widget=CKEditorUploadingWidget())
    content_en = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'is_published', 'updated_at', 'created_at', 'views')
    prepopulated_fields = {'slug': ('title',)}
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    form = PostAdminForm
    list_filter = ('is_published', 'tags')
    readonly_fields = ('views', 'created_at', 'updated_at')


class TagAdmin(TranslationAdmin):
    """Для тэгов"""
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageNewAdmin)

admin.site.site_title = 'Управление публикациями'
admin.site.site_header = 'Управление публикациями'
