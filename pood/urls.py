from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r"^$", views.pood),
    path('toode/<int:toode_id>/', views.toode)
]