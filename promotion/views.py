from django.views.generic import ListView
from .models import Post

class PostList(ListView):
    model = Post
    ordering = '-pk'
    paginate_by = 5
# Create your views here.

