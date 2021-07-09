from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Blogs

def all_blogs(request):
    blogs = Blogs.objects.all()
    return render(request, 'blog/home.html', {'blogs':blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blogs, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':blog})
    
