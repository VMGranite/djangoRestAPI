from django.urls import path
from . import views
from .views import welcome

urlpatterns = [
    path('', welcome, name="welcome"),
    path('get/', views.get_data),
    path('post/', views.post_data),
]
