from django.db import models

from .user import User


class AnnimeVideo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    portrait = models.ImageField(upload_to="annimes/")
    file = models.FileField(upload_to="annimes/")
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    number_of_views = models.PositiveIntegerField(default=0)

    class Meta:
        app_label = "annime"

    def __str__(self):
        return f"{self.author} -> {self.title}"
