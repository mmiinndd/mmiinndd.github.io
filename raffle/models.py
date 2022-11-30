from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    head_image = models.ImageField(upload_to='raffle/images/%Y/%m/%d/', blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[self.title]{self.title}'

    def get_absolute_url(self):
        return f'/raffle/{self.pk}/'

# Create your models here.
