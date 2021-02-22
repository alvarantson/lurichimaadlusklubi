"""LEHT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import reverse

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('index.urls')),
    url(r'^meist/', include('meist.urls')),
    url(r'^treenerid/', include('treenerid.urls')),
    url(r'^pood/', include('pood.urls')),
    url(r'^hinnakiri/', include('hinnakiri.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^tutvustus/', include('tutvustus.urls')),
    url(r'^favicon.ico$',
        RedirectView.as_view( # the redirecting function
            url=staticfiles_storage.url('favicon.png'), # converts the static directory + our favicon into a URL
            # in my case, the result would be http://www.tumblingprogrammer.com/static/img/favicon.ico
        ),
        name="favicon" # name of our view
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
