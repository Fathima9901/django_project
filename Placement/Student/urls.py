from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('login_view', views.login_view, name='login_view'),
    path('student_dashboard', views.student_dashboard, name='Student'),
    path('apply_drive/', views.apply_drive, name='apply_drive'),

]



