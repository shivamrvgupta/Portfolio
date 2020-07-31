from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Job
# Create your views here.


def index(request):
    print("request passed1")
    jobs = Job.objects.order_by('-created_date').filter(is_published=True)
    paginator = Paginator(jobs, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        "jobs": paged_listings
    }
    print("request passed")
    return render(request, 'jobs/jobs.html', context)


def job(request, job_id):

    job = get_object_or_404(Job, pk=job_id)

    context = {
        "job": job
    }

    return render(request, 'jobs/job.html', context)
