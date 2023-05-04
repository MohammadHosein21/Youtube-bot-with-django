from django.shortcuts import render


# Create your views here.

def bot(request):
    return render(request, 'Bot/search.html')
