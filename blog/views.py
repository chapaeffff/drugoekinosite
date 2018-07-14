from django.shortcuts import render, get_object_or_404, redirect
from .models import *

# Create your views here.


def lists(request):
    lists = List.objects.all()
    return render(request, 'blog/lists.html', {'lists':lists})

def list(request, slug):
    cur_list = get_object_or_404(List, slug=slug)
    print (cur_list)
    items = Film_List_Elem.objects.filter(owner_list =cur_list.pk)
    return render(request, 'blog/list.html', {'list': cur_list, 'items':items})