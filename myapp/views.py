from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    a='ram'
    return render(request,"index.html",{'a':'rosh'})