from django.contrib import admin
from .models import JobBlogPost, JobCategory, JobType

admin.site.site_header = "Job Blog Administration"
admin.site.site_title = "Job Blog Admin Portal"
admin.site.register(JobBlogPost)
admin.site.register(JobCategory)
admin.site.register(JobType)
