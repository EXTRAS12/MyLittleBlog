from django.contrib import admin

from .models import Newsletter, NewsletterUser


class NewsletterUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at',)


admin.site.register(Newsletter)
admin.site.register(NewsletterUser, NewsletterUserAdmin)
