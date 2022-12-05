from django.urls import path
# from . import views
from .views import HomeView, ProjectDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('project/<int:pk>', ProjectDetailView.as_view(), name='project-detail'),
]
