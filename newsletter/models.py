from django.db import models


class NewsletterUser(models.Model):
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Newsletter(models.Model):
    EMAIL_STATUS_CHOICE = (
        ('Draft', 'Draft'),
        ('Published', 'Published')
    )
    subject = models.CharField(max_length=255)
    body = models.TextField()
    email = models.ManyToManyField(NewsletterUser)
    status = models.CharField(max_length=10, choices=EMAIL_STATUS_CHOICE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject