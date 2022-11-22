from django.shortcuts import render

def promotion(request):
    return render(
        request,
        'promotion/promotion.html',
    )
# Create your views here.
