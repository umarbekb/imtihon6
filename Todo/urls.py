from django.urls import path
from Todo import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('search/', views.search_todos, name='search_todos'),
    path('filter/', views.filter_todos, name='filter_todos'),
]
