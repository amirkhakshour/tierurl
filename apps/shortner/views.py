from django.shortcuts import render
from django.http.response import HttpResponseNotAllowed, HttpResponseBadRequest
from .services import gen_random_alphanum_string

MESSAGE_INVALID_DATA_PARAMS = b'please send url parameter in your request data.'


def url_shortner_page(request):
    """URL shortner page
    A better option would be to use DJRF serializers and DJRF APiView,
    to remove unnecessary tests, specially validation tests.
    """
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    if request.POST.get('url', None) is None:
        return HttpResponseBadRequest(MESSAGE_INVALID_DATA_PARAMS)

    template = 'shortner/shortner_page.html'
    context = {}
    return render(request, template, context)
