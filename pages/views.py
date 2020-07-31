from django.shortcuts import render
from jobs.models import Job
from blogs.models import Blog
# Create your views here.

def index(request):
    jobs = Job.objects.order_by('-created_date').filter(is_published=True)
    blogs = Blog.objects.order_by('-created_date').filter(is_published=True)

    context={
        'jobs':jobs,
        'blogs':blogs
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')