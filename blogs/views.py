from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator 
from .models import Blog 
# Create your views here.

def blogs(request):
    print("request passed1")
    blogs = Blog.objects.order_by('-created_date').filter(is_published=True)
    paginator = Paginator(blogs, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        "blogs": paged_listings 
    }
    print("request passed")
    return render(request, 'blogs/blogs.html', context) 

def blog(request, blog_id):

    blog = get_object_or_404(Blog, pk=blog_id)

    context = {
        "blog": blog
    }

    return render(request, 'blogs/blog.html', context)
    