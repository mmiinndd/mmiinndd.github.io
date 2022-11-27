from django.shortcuts import render
from .models import Post

def promotion(request):
    posts = Post.objects.all().order_by('-pk')

    return render(
        request,
        'promotion/promotion.html',
        {
            'posts': posts,
        }
    )
# Create your views here.
