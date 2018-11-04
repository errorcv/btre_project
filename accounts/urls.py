from django.urls import path
from django.conf.urls import url, include

from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('metrics', views.metrics, name='metrics'),
    path('deleteJobApplication', views.deleteJobApplication, name='deleteJobApplication'),
    path('updateJobApplication', views.updateJobApplication, name='updateJobApplication'),
    path('filterJobApplications', views.filterJobApplications, name='filterJobApplications'),
    path('addJobApplication', views.addJobApplication, name='addJobApplication'),
    url('', include('social_django.urls', namespace='social')),
    path('dashboard', views.dashboard, name='dashboard')
]
