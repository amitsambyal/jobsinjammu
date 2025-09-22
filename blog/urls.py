
from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>/', views.job_detail, name='job_detail'),
    path('category/<int:category_id>/', views.jobs_by_category, name='jobs_by_category'),
]
# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
