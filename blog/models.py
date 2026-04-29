from django.conf import settings
from django.db import models

class Post(models.Model):
    CATEGORY_CHOICES = [
        ('Motivation', 'Motivation'),
        ('Discipline', 'Discipline'),
        ('Learning', 'Learning'),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='posts/', blank=True, null=True)

    # 🔥 NEW FIELD (important)
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='Learning'
    )

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title