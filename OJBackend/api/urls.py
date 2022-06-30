from django.urls import path
from . import views

urlpatterns = [
    path('problems', views.Problem_post, name='Problem_post'),
    path('problems/<int:id>', views.Problem_detail, name='Problem_detail'),
]
