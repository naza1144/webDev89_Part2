from django.shortcuts import render

# Create your views here.
def componets_view(request):
    return render(request, 'showcases/componnets.html')