"""
URL configuration for class1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from daily_news.views import blog_post, homepage, article, not_found, delete_blog, edit_blog, register, profile
urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include('django.contrib.auth.urls')),
    path("accounts/register", register, name="register"),
    path("new_blog/", blog_post, name="create-blog"),
    path("blog/", blog_post),
    path("article/<int:pk>", article, name="read-blog"),
    path("article/<int:pk>/delete", delete_blog, name="delete_blog"),
    path("article/<int:pk>/edit/", edit_blog, name="edit_blog"),
    path("", homepage, name="home"),
    path("accounts/profile", profile, name="profile"),
    path("not_found", not_found, name="not_found"),

    
]
