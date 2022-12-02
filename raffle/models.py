from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdown

class Post(models.Model):
    title = models.CharField(max_length=50)
    hook_text = models.CharField(max_length=100, blank=True)
    content = MarkdownxField(blank=True)
    images = MarkdownxField(blank=True)
    link = models.TextField(blank=True)


    head_image = models.ImageField(upload_to='raffle/images/%Y/%m/%d/', blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
#    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return f'[{self.pk}]{self.title}'

    def get_absolute_url(self):
        return f'/raffle/{self.pk}/'

    def get_content_markdown(self):
        return markdown(self.content)




class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'
# Create your models here.
