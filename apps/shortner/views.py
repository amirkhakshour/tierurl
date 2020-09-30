from django.http.response import HttpResponseNotAllowed, HttpResponseBadRequest, JsonResponse
from .models import ShortURL
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

    url_to_shorten = request.POST.get('url')

    short_url, created = ShortURL.objects.get_or_create(url=url_to_shorten)

    return JsonResponse({
        'url': short_url.url,
        'tiny_url': short_url.abs_tiny_url,
    })
