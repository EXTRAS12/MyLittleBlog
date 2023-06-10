from modeltranslation.translator import TranslationOptions, register

from .models import Post, Tag


@register(Tag)
class TagTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'content', 'tags')