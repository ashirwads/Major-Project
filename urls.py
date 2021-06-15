from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='website-home'),
    path('aktu/', views.aktu, name='website-aktu'),
    path('siet/', views.siet, name='website-siet'),
    path('contact/', views.contact, name='website-contact'),
    path('course/', views.course, name='website-course'),
    path('admission/', views.admission, name='website-admission'),
    path('fees/', views.fees, name='website-fees'),
    path('circular/', views.circular, name='website-circular'), 
    path('syllabus/', views.syllabus, name='website-syllabus'),
    path('complainbox/', views.complainbox, name='website-complainbox'),




]

  