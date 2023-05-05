import math

from django.shortcuts import render
from .forms import SearchForm
from .bot import search
from .models import Channel
from django.core.paginator import Paginator
from django.shortcuts import redirect


# Create your views here.

def searchView(request):
    if request.method == 'POST':
        keyword = request.POST['keyword']
        results = Channel.objects.filter(keyword=keyword).order_by('-subscriber')
        if len(results) == 0:
            search(keyword)
        request.session['keyword'] = keyword
        return redirect('result-view')
    return render(request, 'Bot/search.html')


def resultView(request):
    keyword = request.session.get('keyword', '')
    results = Channel.objects.filter(keyword=keyword).order_by('-subscriber')
    paginator = Paginator(results, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    page_count = math.ceil(len(results) / 20)
    page_list = []
    for i in range(1, page_count + 1):
        page_list.append(i)
    return render(request, 'Bot/result.html', {'page_obj': page_obj, 'page_list': page_list, 'keyword':keyword})
