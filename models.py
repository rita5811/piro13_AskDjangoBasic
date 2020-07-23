from django.db import models
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, resolve_url

def view1(request):
    return HttpResponse('Hello, Ask Company')
def view2(request):
    return render(request, 'template.html')
def view3(request):
    return JsonResponse({'hello': 'Ask Company'})

def view1(request):
return HttpResponseRedirect('/shop/')
def view2(request):
    url = resolve_url('shop:item_list')
    return HttpResponseRedirect(url)
def view3(request):
    return redirect('shop:item_list')

def view1(request):
    try:
        item = Item.objects.get(pk=100)
    except Item.DoesNotExist:
        raise Http404
def view2(request):
    item = get_object_or_404(Item, pk=100)
def view3(request):
    try:
        item = Item.objects.get(pk=100)
    except Item.DoesNotExist:
        return HttpResponseNotFound()

# Create your models here.
