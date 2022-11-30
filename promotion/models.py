from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdown
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = MarkdownxField()

    head_image = models.ImageField(upload_to='raffle/images/%Y/%m/%d/', blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return f'[{self.pk}]{self.title}'

    def get_content_markdown(self):
        return markdown(self.content)

# Create your models here.
