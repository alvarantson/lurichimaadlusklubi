from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r"^$", views.blog),
    path('<int:post_id>/', views.post)
]