from django.shortcuts import render

# Create your views here.
def returnmain(request):
    return render(request, 'main/index.html')