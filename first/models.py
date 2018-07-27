from django.db import models

# Create your models here.
class Comment(models.Model):
    comment = models.TextField(verbose_name="Comment")

    @property
    def quantity(self):
        return len(set(self.comment.split()))
