from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import DemoItem

# Create your views here.
def componets_view(request):
    return render(request, 'showcases/componnets.html')

def javascrip_view(request):
    return render(request, 'showcases/javascrip.html')

def htmx_demo_view(request):
    demo_items = DemoItem.objects.all()
    return render(request, "showcases/htmx_demo.html", {"demo_items": demo_items, "items": demo_items})

def htmx_search_view(request):
    q = request.GET.get('q', '').strip()
    if q:
        items = DemoItem.objects.filter(title__icontains=q)
    else:
        items = DemoItem.objects.all()
    return render(request, 'showcases/partials/demo_item_list.html', {"items": items, "demo_items": items})

def htmx_item_add_view(request):
    if request.method == 'POST':
        title = request.POST.get("title", "").strip()
        if title:
            DemoItem.objects.create(title=title)

    items = DemoItem.objects.all()
    return render(request, 'showcases/partials/demo_item_list.html', {"items": items, "demo_items": items})

def htmx_item_edit_view(request, pk):
    item = get_object_or_404(DemoItem, pk=pk)
    if request.method == 'POST':
        title = request.POST.get("title", "").strip()
        if title:
            item.title = title
            item.save()
        return render(request, 'showcases/partials/demo_item_row_readonly.html', {"item": item})
    return render(request, 'showcases/partials/demo_item_edit_form.html', {"item": item})

def htmx_item_cancel_view(request, pk):
    item = get_object_or_404(DemoItem, pk=pk)
    return render(request, 'showcases/partials/demo_item_row_readonly.html', {"item": item})

def htmx_item_delete_view(request, pk):
    item_delete = get_object_or_404(DemoItem, pk=pk)
    if request.method == 'POST' or request.method == 'DELETE':
        item_delete.delete()
        return HttpResponse('')
    return HttpResponse('Method Not Allowed', status=405)

def demo_search_view(request):
    req = request.GET
    search = req.get("name", '').strip()
    if search == '':
        items = DemoItem.objects.all()
    else:
        items = DemoItem.objects.filter(title__icontains=search)
    return render(request, 'showcases/partials/demo_item_row_s.html', {"items": items})