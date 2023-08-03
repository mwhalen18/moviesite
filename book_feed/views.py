from django.shortcuts import render

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Book
from .filters import BookFilter

# Create your views here.
def book_list(request):
    f = BookFilter(request.GET, queryset=Book.objects.all().order_by('title'))    
    #query_set = Book.objects.all().order_by('title')
    paginator = Paginator(f.qs, 20)

    page = request.GET.get('page')

    try:
        response = paginator.page(page)
    except PageNotAnInteger:
        response = paginator.page(1)
    except EmptyPage:
        response = paginator.page(paginator.num_pages)



    context = {
        'filter': response,
        'filtered_qs_form': f
    }

    return render(request, 'book_feed/book_list.html', context)