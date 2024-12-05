# management/urls.py
from django.urls import path
from .views import (
    ClientListCreateView,
    ClientRetrieveUpdateDestroyView,
    ProjectListCreateView,
    UserAssignedProjectsView,
)

urlpatterns = [
    path('clients/', ClientListCreateView.as_view(), name='client-list-create'),  
    path('clients/<int:pk>/', ClientRetrieveUpdateDestroyView.as_view(), name='client-detail'),
    path('clients/<int:client_id>/projects/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('projects/', UserAssignedProjectsView.as_view(), name='user-projects'),

]
