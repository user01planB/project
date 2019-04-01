from django.shortcuts import render
from .models import Post
# Create your views here.

def list_of_post(request):
    post = Post.objects.all()
    template = '/django/blog/cms/blog/templates/blog/list_of_post.html'
    context = {'post': post}
    return render(request, template, context)
    