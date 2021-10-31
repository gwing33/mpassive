"""
To render HTML webpages
"""

from django.http import HttpResponse


def home_view(request):
    """
    Take in a request (Django sends in request)
    Return HTML as a response
    """
    name = 'World'
    html = f"""
    <h1>Hello {name}!</h1>
    """
    return HttpResponse(html)
