from django.shortcuts import render
from django.views.generic import View
from apps.blog.forms import PosCreateForms
# Create your views here.

class BloglistView(View):
    def get(self, request, *args, **kwargs):
        context={
            
        }
        return render(request, 'index.html',context )

class BlogCreateView(View):
    def get(self, request, *args, **kwargs):
        context={
            
        }
        return render(request, 'blog_create.html',context )
    def get(self, request, *args, **kwargs):
        context={
            
        }
        return render(request, 'blog_create.html',context )