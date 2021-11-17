from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post

# Create your views here.
def blogHome(request):
    # return HttpResponse("This is Blog Home Page")
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request, 'blog/BlogHome.html', context)

def blogPost(request, slug):
    # return HttpResponse(f'This is Blog Slug Page And your slug is : {slug}')
    post  = Post.objects.filter(slug=slug).first()
    context = {'post' : post}
    return render(request, 'blog/BlogPost.html', context)