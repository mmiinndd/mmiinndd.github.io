from django.views.generic import ListView, DetailView
from .models import rafflepost

class PostList(ListView):
    model = rafflepost
    ordering = '-pk'

class PostDetail(DetailView):
    model = rafflepost

# Create your views here.
