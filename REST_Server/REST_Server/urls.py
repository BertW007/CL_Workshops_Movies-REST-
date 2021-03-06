"""REST_Server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from movies.views import MovieView,MoviesView,PersonView,PersonsView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^movies/$', MoviesView.as_view(), name='movies-all'),
    url(r'^movie/(?P<id>(\d)+)$', MovieView.as_view(), name='movie-details'),
    url(r'^persons/$', PersonsView.as_view(), name='persons-all'),
    url(r'^person/(?P<id>(\d)+)$', PersonView.as_view(), name='person-details'),
]
