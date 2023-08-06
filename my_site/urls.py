"""Disney URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from des.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page,name='main_page'),
    path('signup/', signup,name='signup'),
    path('login/', login_page,name='login_page'),
    path('movie/', movie,name='movie'),
    path('logout/', logout_page,name='logout_page'),
    path('myprofile/',my_profile,name='my_profile'),
    path('view_movies/<id>/',view_movies,name='view_movies'),
    path('marver_movies/',marver_movies,name='marver_movies'),
    path('p_movies/',Pixar_movies,name='Pixar'),
    path('d_movies/',Disney_movies,name='Disney'),
    path('n_g_movies/',N_G_movies,name='National Geographic'),
    path('Star_Wars_movies/',Star_movies,name='Star Wars'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
