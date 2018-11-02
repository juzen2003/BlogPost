"""davetestblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path
import posts.views
import sitepages.views
from django.conf.urls import url
# for showing static images
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^$', views.home)
    path('', posts.views.home, name='home'),
    # different ways to define url
    # url(r'^posts/(?P<post_id>[0-9]+)/$', posts.views.posts_detail),
    # re_path(r'^posts/(?P<post_id>[0-9]+)/$', posts.views.posts_detail),
    path('posts/<int:post_id>/', posts.views.posts_detail, name='post_detail'),
    path('about/', sitepages.views.about, name='about'),

    # static part is for displaying static image on the page, define the path in settings
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
