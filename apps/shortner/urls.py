from django.urls import path
from shortner.views import url_shortner_page
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('shortner', csrf_exempt(url_shortner_page), name='shortner-page')
]
