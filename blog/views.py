from django.http.request import HttpHeaders
from django.shortcuts import render
from blog.models import Blog

def blog(request):
    # data = {'name': 'Slava', 'age': 84}
    qs = Blog.objects.all()
    context = {'objects_list': qs}
    return render(request, 'blog/home.html', context)

