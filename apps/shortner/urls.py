from django.urls import path
from shortner.views import url_shortner_page

urlpatterns = [
    path('shortner', url_shortner_page, name='shortner-page')
]
