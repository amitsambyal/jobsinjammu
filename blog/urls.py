

from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>/', views.job_detail, name='job_detail'),
    path('category/<int:category_id>/', views.jobs_by_category, name='jobs_by_category'),
]
