# from django.conf.urls import url
# # from . import views
# from views import home_view, login_view, signup_view, services_view, contact_view, amc_view
#
# urlpatterns = [
#     # url(r'^$', views.index, name='index')
#     url(r'^amc', amc_view),
#     url(r'^contact', contact_view),
#     url(r'^services', services_view),
#     url(r'^login', login_view),
#     url(r'^signup', signup_view),
#     url(r'^$', home_view),
# ]

from django.conf.urls import url
from . import views
# from .views import home_view, login_view, signup_view, services_view, contact_view, amc_view
#
urlpatterns = [
    # url(r'^$', views.index, name='index')
    url(r'^about', views.about_view, name='about_view'),
    url(r'^amc', views.amc_view, name='amc_view'),
    url(r'^contact', views.contact_view, name='contact_view'),
    url(r'^services', views.services_view, name='services_view'),
    url(r'^login', views.login_view, name='login_view'),
    url(r'^signup', views.signup_view, name='signup_view'),
    url(r'^$', views.home_view, name='home_view'),
]

