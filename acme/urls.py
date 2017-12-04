"""acme URL Configuration

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
from acme_app.views import home_view, login_view, signup_view, services_view, contact_view, amc_view, about_view

urlpatterns = [
    url(r'^about', about_view),
    url(r'^amc', amc_view),
    url(r'^contact', contact_view),
    url(r'^services', services_view),
    url(r'^login', login_view),
    url(r'^signup', signup_view),
    url(r'^$', home_view),
    url(r'^admin/', admin.site.urls),
    url(r'^$', include('acme_app.urls')),
    # url(r'^jet/', include('jet.urls', 'jet')),
]
