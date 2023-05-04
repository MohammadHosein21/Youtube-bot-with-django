from django.shortcuts import render
from .forms import SearchForm
from .bot import search
from .models import Channel


# Create your views here.

def search(request):
    if request.method == 'POST':
        keyword = request.POST['keyword']
        results = Channel.objects.filter(keyword=keyword).order_by('-subscriber')
        # form = request.POST['keyword']
        # if form.is_valid():
        #     keyword = form.cleaned_data['keyword']
        #     results = Channel.objects.filter(keyword=keyword).order_by('-subscriber')
        if len(results) == 0:
            results = search(keyword)
        return render(request, 'Bot/result.html', {'results': results})
    else:
        form = SearchForm()
    return render(request, 'Bot/search.html', {'form': form})
