from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.text import slugify

class JobCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Job Categories"

    def __str__(self):
        return self.name


# 🔹 Job Type Model
class JobType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class JobBlogPost(models.Model):
    job_type = models.ForeignKey(JobType, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)
    job_category = models.ForeignKey(JobCategory, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True, null=True)
    blog_detail = CKEditor5Field(
        help_text="Detailed description of the blog", 
        config_name='extends',
        default="No description provided."
        )
    published_date = models.DateTimeField(auto_now_add=True)
    popular_post = models.BooleanField(default=False)
        
    def __str__(self):
        return self.job_title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            # generate slug from job title
            self.slug = slugify(self.job_title)
        super().save(*args, **kwargs)
   
    
