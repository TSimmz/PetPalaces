"""
Definition of urls for PetPalaces.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from pages.views import home_view, shop_view, customize_view, contact_view, about_view

urlpatterns = [

    # New URLS
    path('', home_view, name='home'),
    path('home/', home_view, name='home'),
    path('shop/', shop_view, name='shop'),
    path('customize/', customize_view, name="customize"),
    path('contact/', contact_view, name='contact'),
    path('about/', about_view, name='about'),
    path('login/',
        LoginView.as_view
        (
            template_name='pages/login.html',
            authentication_form=forms.BootstrapAuthenticationForm,
            extra_context=
            {
                'title': 'Log in',
                'year' : datetime.now().year,
            }
        ),
        name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]
