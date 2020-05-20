from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
def home_view(request, *args, **kwargs):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'pages/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )