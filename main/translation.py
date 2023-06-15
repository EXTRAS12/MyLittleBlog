from modeltranslation.translator import TranslationOptions, register

from .models import FlatPage, NewFlatpage, Post, Tag


@register(Tag)
class TagTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'content', 'tags')


@register(FlatPage)
class FlatPageTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(NewFlatpage)
class NewFlatPageTranslationOptions(TranslationOptions):
    fields = ('description', 'text_block')
