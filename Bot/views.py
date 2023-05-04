from django.shortcuts import render
from .forms import SearchForm
from .bot import search
from .models import Channel
from django.core.paginator import Paginator


# Create your views here.

def searchView(request):
    if request.method == 'POST':
        keyword = request.POST['keyword']
        results = Channel.objects.filter(keyword=keyword).order_by('-subscriber')
        # form = request.POST['keyword']
        # if form.is_valid():
        #     keyword = form.cleaned_data['keyword']
        #     results = Channel.objects.filter(keyword=keyword).order_by('-subscriber')
        if len(results) == 0:
            results = search(keyword)
        paginator = Paginator(results, 20)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'Bot/result.html', {'results': results, 'page_obj': page_obj})
    else:
        form = SearchForm()
    return render(request, 'Bot/search.html', {'form': form})
