from django.shortcuts import render

# Create your views here.

def base(request):
    return render(
        request,
        'raffle/raffle.html',
    )

def detail(request):
    return render(
        request,
        'raffle/detail.html',
    )


