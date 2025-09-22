from django.shortcuts import render, get_object_or_404
from .models import JobBlogPost, JobCategory
from django.db.models import Q
# Create your views here.


def index(request):
    jobs = JobBlogPost.objects.all().order_by('-published_date')
    categories = JobCategory.objects.all()
    return render(request, 'blog/index.html', {'jobs': jobs, 'categories': categories})

def job_detail(request, slug):
    job = get_object_or_404(JobBlogPost, slug=slug)
    related_jobs = JobBlogPost.objects.filter(
        job_category=job.job_category
    ).exclude(id=job.id)[:7]
    return render(request, "blog/job_detail.html", {
        "job": job,
        "related_jobs": related_jobs
    })
def jobs_by_category(request, category_id):
    category = get_object_or_404(JobCategory, id=category_id)
    jobs = JobBlogPost.objects.filter(job_category=category)
    categories = JobCategory.objects.all()
    return render(request, 'blog/index.html', {'jobs': jobs, 'categories': categories, 'selected_category': category})

def job_search(request):
    query = request.GET.get('q')  # 'q' is the name of the search input
    results = []
    if query:
        results = JobBlogPost.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
    return render(request, 'blog/job_search.html', {
        'query': query,
        'results': results
    })