from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
def home_view(request, *args, **kwargs):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'pages/home.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def shop_view(request, *args, **kwargs):
    """Renders the shop page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'pages/about.html',
        {
            'title':'Shop',
            'message':'Your application shop page.',
            'year':datetime.now().year,
        }
    )

def customize_view(request, *args, **kwargs):
    """Renders the customize page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'pages/customize.html',
        {
            'title':'Customize',
            'year':datetime.now().year,
        }
    )

def contact_view(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'pages/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about_view(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'pages/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )