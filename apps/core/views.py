from django.shortcuts import render

# Create your views here.


def frontpage(request):
    context = {}
    return render(request,'core/base.html' , context=context) 